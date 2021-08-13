# REQUIREMENTS

This project only requires your system to have [python 3](https://www.python.org/downloads/) installed. 
It should run on all major OS.

# INSTALLATION

Download the project as `.zip` archive and extract it, or clone it with git:

`git clone https://github.com/michalmasrna1/skusac.git`

Enter the project directory:

`cd skusac`

Run `main.py` with python:

`python main.py` or `python3 main.py`

# USAGE

This software provides a platform for testing the user for their knowledge of simple question answer pairs. These are 
provided in a simple text file, for more detail see the [Q&A files section](#qa-files)

## Settings

The testing process is customizable to some extent. All settings are controlled by the values set in the
`settings.py` file. The user can modify these settings to fit their need.

#### CONSTANTS

At the beginning of the file some constants are defined, there is no need to change this section.

#### Q&A FILE SETTINGS

Section containing settings regarding the text files with question answer pairs.

Q_A_DIR - the name of the directory containing the text files with questions

- empty string if the text files are in the same directory as main.py

Q_A_FILENAME - the name of the text file containing the question answer pairs

#### EXAM SETTINGS

This is the section containing the core of the settings regarding the testing process.

DIRECTION - decides what the user is asked and what are they to provide
 - ONE_WAY - the user is asked a question and shall respond with the answer
 - REVERSED - the user is prompted with the answer and provides the question
 - TWO_WAY - the user is prompted with both the questions and the answers


EXAM_MODE - decides how the pool of questions is generated and maintained
 - RANDOM - each question is picked separately, at random from the entire set
 - QUEUE - the questions are shuffled at the beginning an then asked each once
 - DISTRIBUTED - the pool is created in the same way as in the QUEUE option, but for each mistake, three copies of the 
question are added to the pool

STRICT_MODE - decides if diacritics, spaces, typos etc. are ignored or not
 - True - the entered string has to match the expected answer exactly
 - False - diacritics, spaces, typos etc. are ignored

## Q&A files

The Q&A text files need to have a precise format in order to be processed correctly. The files consist of question and 
answer pairs. Each such pair is separated by exactly one empty line before and after. The question has to fit into one 
line, the answer can span over multiple lines, with no empty line between the question and the answer. The answer 
(or the question) can contain multiple correct answers. Such multiple entries need to be separated by a comma (`,`).

#### Special lines

Except for the question and answer pairs, the text file can contain two special lines:

`#!START` - Implicitly at the beginning of the file

`#!END` - Implicitly at the end of the file

Only questions before the first `#!END` line and after the last `#!START` line (last, which came before the first
`#!END`) will be processed and tested.

These lines cannot contain anything else (except for leading and trailing spaces). They do as well have to be separated
by one empty line before and after the special line.


## The testing process

During the testing process, the user is prompted with a question (or an answer, see setting [DIRECTION](#exam-settings))
and has to respond with the appropriate answer (or question respectively). If the response is correct, next prompt is 
printed. If the response is only partially correct (only one of possible answers is provided, or there is a typo in the
response etc.), the full, correct answer is printed in green. Otherwise, if the response was incorrect, the correct 
answer is printed in red.

#### Special responses

The user can also provide one of the two special responses:

`q` - if the response is only one character `q`, the testing process as well as the program will end immediately.

`#` - if the response starts with `#` character, the number of questions left in the question pool is printed. However, 
the rest of the response (without the first character) is treated as a normal response.