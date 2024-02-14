from random import randint


MESSEGE = 'Find the greatest common divisor of given numbers.'


def gcd(first, second):
    """Функция принимает на вход два числа
    и находит наибольший общий делитель этих чисел."""  # НОД
    while second > 0:
        first, second = second, first % second
    return first


def game():
    """Функция создает два случайных числа(1, 100)
    передает их в функцию gcd, и возвращает это число
    и правильный ответ."""
    random_numb_first = randint(1, 100)
    random_numb_second = randint(1, 100)

    question = f'{random_numb_first} {random_numb_second}'
    right_answer = str(gcd(random_numb_first, random_numb_second))
    return question, right_answer
