def engine(question, right_answer):
    print(f'Question: {question}')
    answer = input('Your answer: ')

    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{right_answer}'.")
        return False
