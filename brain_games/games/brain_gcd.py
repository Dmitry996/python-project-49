from math import gcd
from random import randint
from brain_games.cli import welcome_user
from brain_games.engine import engine


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    
    round = 0

    while round < 3:
        random_numb_first = randint(1, 100)
        random_numb_second = randint(1, 100)

        question = f'{random_numb_first} {random_numb_second}'
        right_answer = str(gcd(random_numb_first, random_numb_second))
        flag = engine(question, right_answer, name)
        if not flag:
            return None

        round += 1
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
