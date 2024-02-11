from random import randint, choice
from brain_games.scripts.brain_games import greeting
from brain_games.engine import engine

symbol_set = ('+', '-', '*')


def calc(first, symbol, second):
    if symbol == '+':
        return first + second
    elif symbol == '-':
        return first - second
    elif symbol == '*':
        return first * second


def brain_calc():
    name = greeting()

    print('What is the result of the expression?')

    count = 0

    while count < 3:
        random_numb_first = randint(1, 100)
        random_numb_second = randint(1, 100)
        symbol = choice(symbol_set)

        question = f'{random_numb_first} {symbol} {random_numb_second}'
        print(f'Question: {question}')

        right_answer = calc(random_numb_first, symbol, random_numb_second)
        user_answer = int(input('Your answer: '))

        flag = engine(user_answer, right_answer, name)

        if not flag:
            return None

        count += 1
    print(f'Congratulations, {name}')


def main():
    brain_calc()


if __name__ == '__main__':
    main()
