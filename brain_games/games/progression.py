from random import randint, choice

MESSEGE = 'What number is missing in the progression?'


def sequence_generator():
    begin = randint(1, 50)
    step = randint(2, 10)
    end = begin + step * 11  # Увеление длинный последовательности на 11

    result = [str(i) for i in range(begin, end, step)]
    elem = choice(result)
    result[result.index(elem)] = '..'
    return ' '.join(result), elem


def game():
    question, right_answer = sequence_generator()
    return question, right_answer
