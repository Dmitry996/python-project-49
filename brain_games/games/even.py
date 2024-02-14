from random import randint

MESSEGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(numb: int) -> bool:
    """функция проверяет четное ли число."""
    return numb % 2 == 0


def game():
    """Функция создает случайное число(1, 100)
    и передает его функции is_even,
    возвращает число и правильный ответ."""
    question = randint(1, 100)
    right_answer = 'yes' if is_even(question) else "no"
    return question, right_answer
