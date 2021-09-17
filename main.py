import hashlib
from pathlib import Path
from typing import Dict, Set, Generator

import htmlmin
from bs4 import BeautifulSoup

QUESTION_TAG_CLASS = 'qtext'
RIGHT_ANSWER_TAG_CLASS = 'rightanswer'
USED_PARSER = 'html5lib'
BASE_HTML = Path('base.html').read_text(encoding='utf-8')


def get_files_content(file_list: Generator[Path, None, None]) -> Dict[str, str]:
    return {str(file): file.read_text(encoding='utf-8') for file in file_list}


def load_soup(file_content: str) -> BeautifulSoup:
    minified_html = htmlmin.minify(file_content, remove_empty_space=True)
    return BeautifulSoup(minified_html, features=USED_PARSER)


def normalize_answer_language(answer_tag: BeautifulSoup) -> BeautifulSoup:
    return BeautifulSoup(str(answer_tag).replace('The correct answer is:', 'Odpowiedź:')
                         .replace('Poprawna odpowiedź to:', 'Odpowiedź:'), features='html.parser'
                         )


def load_tags_map(soup: BeautifulSoup) -> Dict[bytes, Dict[str, BeautifulSoup]]:
    question_tags = soup.findAll('div', {'class': QUESTION_TAG_CLASS})
    right_answer_tags = soup.findAll('div', {'class': RIGHT_ANSWER_TAG_CLASS})
    return {
        hashlib.md5(str(question_tag).encode('utf-8')).digest(): {
            'question_tag': question_tag,
            'answer_tag': normalize_answer_language(answer_tag)
        } for question_tag, answer_tag in zip(question_tags, right_answer_tags)
    }


def show_already_hashed(file_path: str, already_hashed: Set[bytes], currently_hashed: Set[bytes]):
    number_of_already_hashed = len(already_hashed.intersection(currently_hashed))
    print(f"Number of already hashed questions from file: {file_path} is: {number_of_already_hashed}")


def save_answers(whole_map: Dict[bytes, Dict[str, BeautifulSoup]]):
    output_soup = BeautifulSoup(BASE_HTML, features=USED_PARSER)
    styles = Path('styles.css').read_text(encoding='utf-8')
    style = output_soup.find('style')
    style.append(styles)
    content = output_soup.find('div', {'class': 'content'})
    for key, tags in whole_map.items():
        question_content_tag = output_soup.new_tag('div', attrs={'class': "question_content"})
        question_content_tag.append(tags['question_tag'])
        question_content_tag.append(tags['answer_tag'])
        content.append(question_content_tag)
    Path('answers.html').write_text(str(output_soup), encoding='utf-8')


def main():
    questions_answers_map = {}
    files_to_analyze = Path('files_to_analyze').glob('*')
    files_content = get_files_content(files_to_analyze)
    for file_path, file_content in files_content.items():
        soup = load_soup(file_content)
        current_file_questions_answers_map = load_tags_map(soup)
        show_already_hashed(file_path, set(questions_answers_map.keys()),
                            set(current_file_questions_answers_map.keys()))
        questions_answers_map.update(current_file_questions_answers_map)
    save_answers(questions_answers_map)


if __name__ == '__main__':
    main()
