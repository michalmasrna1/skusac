from typing import List, Tuple, Optional
from random import randint, choice, shuffle
from os import path

from settings import *
from characters import CHARACTERS

Question = Tuple[str, str]
Q_A = List[Question]


def load_q_a(filename: str) -> Q_A:
    with open(filename) as file:
        questions = file.read().split('\n\n')

    q_a: List[Tuple[str, str]] = []
    for question in questions:
        if question.strip() == '#!START':
            q_a = []
            continue
        elif question.strip() == '#!END':
            break
        end_of_question = question.index('\n')
        q_a.append((question[:end_of_question], question[end_of_question + 1:].strip()))

    return q_a


def init_pool(q_a: Q_A, mode: int) -> Q_A:
    if mode == RANDOM:
        return []
    if mode == QUEUE:
        pool = q_a.copy()
        shuffle(pool)
        return pool
    if mode == DISTRIBUTED:
        pool = q_a.copy()
        shuffle(pool)
        return pool


def get_question_answer(q_a: Q_A, pool: Q_A, last_question: Optional[Question], correct: bool, mode: int) -> Question:
    if mode == RANDOM:
        return choice(q_a)
    if mode == QUEUE:
        if not pool:
            print('You won!')
            exit(0)
        return pool.pop()
    if mode == DISTRIBUTED:
        if not correct:
            pool += [last_question, last_question, last_question]
        if not pool:
            print('You won!')
            exit(0)
        question = choice(pool)
        pool.remove(question)
        return question


def normalize(string: str) -> str:
    string = string.lower()
    new_string = ''
    prev_char = ''
    for char in string:
        if char in CHARACTERS:
            new_string += CHARACTERS[char]
        else:
            if not char.isspace() and not char == prev_char:
                new_string += char
        prev_char = char
    return new_string


def check_answer(response: str, answer: str) -> bool:
    if response == answer:
        return True
    answer_orig = answer
    if not STRICT_MODE:
        answer = normalize(answer)
        response = normalize(response)
    answers = answer.split(',')
    answers = [ans.strip() for ans in answers]
    if response in answers:
        print(f"\033[92m{answer_orig}\033[00m")
        return True
    else:
        print(f"\033[91m{answer_orig}\033[00m")
        return False


def main() -> None:
    q_a = load_q_a(path.join(path.dirname(path.abspath(__file__)), Q_A_DIR, Q_A_FILENAME))
    pool = init_pool(q_a, EXAM_MODE)
    last_question: Optional[Question] = None
    correct = True

    while True:
        question, answer = get_question_answer(q_a, pool, last_question, correct, EXAM_MODE)
        last_question = (question, answer)

        if DIRECTION == TWO_WAY and randint(0, 1) or DIRECTION == REVERSED:
            question, answer = answer, question

        print(question)
        response = input().strip()
        if response == 'q':
            exit(0)
        if response.startswith('#'):
            print(len(pool))
            response = response[1:].strip()
        correct = check_answer(response, answer)
        print()


main()
