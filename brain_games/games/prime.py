from random import randint

MESSEGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numb):
    max_possible_divisor = int(numb ** 0.5 + 1)
    for i in range(2, max_possible_divisor):
        if numb % i == 0:
            return False
    return True


def game():
    question = randint(2, 1000)
    right_answer = 'yes' if is_prime(question) else "no"
    return question, right_answer
