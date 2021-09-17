### Moodle Rearrange exam questions to fast check
@reverse-developer

This is HTML scraping of [Moodle](https://moodle.org/) based university e-learning platforms post-exam review system.

### What is this script for?
Your group just finished first try on your tests with closed-ended questions. 50 of them, to finish in 1 hour.

It's nearly impossible to do so without knowing every question beforehand - so you collaborate.

But, surprise, questions are mixed so it's hard to help each other.

So you finish it with merely 50% of answers being correct.

Sure, you passed, but you know you could do better if this test set wasn't so bull**** with no real world meaning.

But wait, there is a way!

There is review button after the test, so you can see ALL of questions with their correct answers!
Saving this won't help you next time though. 

You would need to just get all possible answers from everyone, meaning maybe 40-50 or even more people.
Also browsing through every one of them would be painful, especially when you cannot find this one pesky question in hundred or maybe even thousand of them.

And, DAMN IT, some of them have pictures inside and THE SAME starting text - meaning even searching for them makes it hard to do.

### So what can I do?
Fear not! I'm coming!
You probably already guessed that the best way would be to aggregate all of those questions into one file.
This is where this script presented to you comes in!

### Prerequisites
* The hardest part - collaborate with your colleagues.
* Everyone needs to save his/her review page with every question shown as HTML file.
* Collect them and provide as an input to this script. Currently it needs to be folder 'files_to_analyze'.
* Simply run it. It will generate simple answers.html file, with all non-repeating ones.
Then you can just browse through it and find the question you wanted.

### Usage
Requires Python and some libraries. Tested on Python 3.8, but should work on any Python 3.x.
Run below from command line. Assuming that `python` is the one Python instance you want to populate with libraries required.

    python -m pip install -r requirements.txt
    python main.py

### Roadmap
* Add styling for answers
* Add search bar, based on parts of the question
* Add simple gui for getting input files and where to generate output
* After above - pyinstaller with .exe file
* Create simple Chrome/Firefox extension which would help with finding questions based on generated hash
* Search bar also based on hash
* By the end - don't show all the questions, just search bar based on hash or part of the question text