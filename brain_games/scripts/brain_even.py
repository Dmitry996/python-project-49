from random import randint
from brain_games.scripts.brain_games import greeting
from brain_games.engine import engine


def brain_even():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count = 0

    while count < 3:
        question = randint(1, 100)
        print(f'Question: {question}')

        user_answer = input('Your answer: ')
        right_answer = 'yes' if question % 2 == 0 else "no"

        flag = engine(user_answer, right_answer, name)

        if not flag:
            return None

        count += 1
    print(f'Congratulations, {name}')


def main():
    brain_even()


if __name__ == '__main__':
    main()
