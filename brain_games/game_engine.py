from prompt import string
from brain_games.cli import welcome_user


def engine(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.MESSEGE)

    round = 0

    while round < 3:
        question, right_answer = game.game()
        print(f'Question: {question}')
        answer = string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return None

        round += 1
    print(f'Congratulations, {name}!')
