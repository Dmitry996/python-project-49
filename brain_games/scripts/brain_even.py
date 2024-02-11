from random import randint
from brain_games.scripts.brain_games import greeting


def brain_even():
    name = greeting()

    print('Answer "yes" if the number is even, otherwise answer "no"')

    count = 0

    while count < 3:
        random_numb = randint(1, 100)
        print(f'Question: {random_numb}')

        answer = input('Your answer: ')
        right_answer = 'yes' if random_numb % 2 == 0 else "no"

        if right_answer != answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print("Let's try again, Bill!")
            return None

        print('Correct!')
        count += 1
    print(f'Congratulations, {name}')


def main():
    brain_even()


if __name__ == '__main__':
    main()
