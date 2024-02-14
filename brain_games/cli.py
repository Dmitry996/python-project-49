from prompt import string


def welcome_user():
    '''Функция приветствия игрока .
    в нутри себя принимает имя и возвращает его .'''
    name = string('May I have your name? ')
    print(f'Hello, {name}')
    return name
