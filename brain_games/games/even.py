from random import randint

MESSEGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(numb: int) -> bool:
    return numb % 2 == 0


def game():
    question = randint(1, 100)
    right_answer = 'yes' if is_even(question) else "no"
    return question, right_answer
