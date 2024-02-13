from random import randint, choice

symbol_set = ('+', '-', '*')

MESSEGE = 'What is the result of the expression?'


def calc(first, symbol, second):
    if symbol == '+':
        return first + second
    elif symbol == '-':
        return first - second
    elif symbol == '*':
        return first * second


def game():

    random_numb_first = randint(1, 100)
    random_numb_second = randint(1, 100)
    symbol = choice(symbol_set)

    question = f'{random_numb_first} {symbol} {random_numb_second}'
    right_answer = str(calc(random_numb_first, symbol, random_numb_second))
    return question, right_answer
