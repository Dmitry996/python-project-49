from random import randint
from brain_games.cli import welcome_user
from brain_games.engine import engine


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    round = 0

    while round < 3:
        question = randint(1, 100)
        right_answer = 'yes' if question % 2 == 0 else "no"
        flag = engine(question, right_answer, name)
        if not flag:
            return None
        round += 1
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
