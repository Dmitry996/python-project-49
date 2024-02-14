from random import randint

MESSEGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numb):
    """Функция проверяет является ли число простым."""
    if numb < 2:
        return False
    max_possible_divisor = int(numb ** 0.5 + 1)
    for i in range(2, max_possible_divisor):
        if numb % i == 0:
            return False
    return True


def game():
    """Функция создает случайное число(2, 1000)
    и передает его функции is_prime,
    возвращает число и правильный ответ."""
    question = randint(2, 1000)
    right_answer = 'yes' if is_prime(question) else "no"
    return question, right_answer
