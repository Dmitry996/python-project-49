from random import randint, choice

symbol_set = ('+', '-', '*')

MESSEGE = 'What is the result of the expression?'


def calc(first, symbol, second):
    """Функция принимает в себя два числа и математический символ,
    и выполняет математическую операцию согласно символу."""
    if symbol == '+':
        return first + second
    elif symbol == '-':
        return first - second
    elif symbol == '*':
        return first * second


def game():
    """Функция создает два случайных числа(1, 100)
    и случайный символ из symbol_set,
    передает их в функцию calc, и возвращает строку математической задачи
    и правильный ответ."""
    random_numb_first = randint(1, 100)
    random_numb_second = randint(1, 100)
    symbol = choice(symbol_set)

    question = f'{random_numb_first} {symbol} {random_numb_second}'
    right_answer = str(calc(random_numb_first, symbol, random_numb_second))
    return question, right_answer
