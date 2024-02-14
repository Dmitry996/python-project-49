from random import randint, choice

MESSEGE = 'What number is missing in the progression?'


def game():
    """Функция создвет случайную равно возрастающую прогрессию чисел
    и возвращает ее с пропущеным элементом и этот элемент отдельно."""
    begin = randint(1, 50)
    step = randint(2, 10)
    end = begin + step * 11  # Увеление длинный последовательности на 11

    result = [str(i) for i in range(begin, end, step)]
    right_answer = choice(result)
    result[result.index(right_answer)] = '..'
    return ' '.join(result), right_answer
