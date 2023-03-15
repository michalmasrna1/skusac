###############################################################################
# CONSTANTS - NO NEED CHANGE
###############################################################################

# DIRECTION
ONE_WAY, REVERSED, TWO_WAY = 0, 1, 2

# EXAM_MODE
RANDOM, QUEUE, DISTRIBUTED = 0, 1, 2

###############################################################################
# Q&A FILE SETTINGS
###############################################################################

# Q_A_DIR - the name of the directory containing the text files with questions
#         - empty string if the text files are in the same directory as main.py
Q_A_DIR = 'q_a'

# Q_A_FILENAME - the name of the text file containing the question answer pairs
Q_A_FILENAME = 'example.txt'

###############################################################################
# EXAM SETTINGS
###############################################################################

# DIRECTION - decides what the user is asked and what are they to provide
#   ONE_WAY - the user is asked a question and shall respond with the answer
#   REVERSED - the user is prompted with the answer and provides the question
#   TWO_WAY - the user is prompted with both the questions and the answers

DIRECTION = ONE_WAY

# EXAM_MODE - decides how the pool of questions is generated and maintained
#   RANDOM - each question is picked separately, at random from the entire set
#   QUEUE - the questions are shuffled at the beginning and then asked each once
#   DISTRIBUTED - the pool is created in the same way as in the QUEUE option,
#      but for each mistake, three copies of the question are added to the pool

EXAM_MODE = DISTRIBUTED

# STRICT_MODE - decides if diacritics, spaces, typos etc. are ignored or not
#   True - the entered string has to match the expected answer exactly
#   False - diacritics, spaces, typos etc. are ignored

STRICT_MODE = True
