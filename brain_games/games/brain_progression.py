from random import randint, choice
from brain_games.cli import welcome_user
from brain_games.engine import engine


def sequence_generator():
    begin = randint(1, 50)
    step = randint(2, 10)
    end = begin + step * 11  # Увеление длинный последовательности на 11

    result = [str(i) for i in range(begin, end, step)]
    elem = choice(result)
    result[result.index(elem)] = '..'
    return ' '.join(result), elem


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    round = 0

    while round < 3:
        question, right_answer = sequence_generator()
        flag = engine(question, right_answer, name)
        if not flag:
            return None

        round += 1
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
