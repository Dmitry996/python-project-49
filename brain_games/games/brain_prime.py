from random import randint
from brain_games.cli import welcome_user
from brain_games.engine import engine


def is_prime(numb):
    max_possible_divisor = int(numb ** 0.5 + 1)
    for i in range(2, max_possible_divisor):
        if numb % i == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    round = 0
    while round < 3:
        question = randint(2, 1000)
        right_answer = 'yes' if is_prime(question) else "no"
        flag = engine(question, right_answer, name)
        if not flag:
            return None
        round += 1
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
