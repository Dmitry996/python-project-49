from random import randint, choice
from brain_games.cli import welcome_user
from brain_games.engine import engine

symbol_set = ('+', '-', '*')


def calc(first, symbol, second):
    if symbol == '+':
        return first + second
    elif symbol == '-':
        return first - second
    elif symbol == '*':
        return first * second


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()

    print('What is the result of the expression?')

    round = 0

    while round < 3:
        random_numb_first = randint(1, 100)
        random_numb_second = randint(1, 100)
        symbol = choice(symbol_set)

        question = f'{random_numb_first} {symbol} {random_numb_second}'
        right_answer = str(calc(random_numb_first, symbol, random_numb_second))
        flag = engine(question, right_answer, name)
        if not flag:
            return None

        round += 1
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
