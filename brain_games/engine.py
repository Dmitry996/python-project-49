def engine(answer, right_answer, name):
    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {name}!")
        return False
