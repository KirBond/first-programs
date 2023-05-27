import random as r

print('Добро пожаловать в числовую угадайку!')

def start():
    answer = input('Вы сами выберите границы или нам сделать это автоматически?(сам/автоматически)\n')
    while answer.lower() != 'сам' and answer.lower() != 'автоматически':
        answer = input(
            'Вы ввели неправильную команду. Вы сами выберите границы или нам сделать это автоматически?(сам/автоматически):\n')
    if answer.lower() == 'сам':
        left = input('Введите левую границу диапазона: \n')
        self(left)
    elif answer.lower() == 'автоматически':
        response = input('Введите число от 1 до 100: \n')
        play_auto(response)

def self(left):
    neg_num = left.startswith('-') and left[1:].isdigit()
    pos_num = left.isdigit()
    while neg_num == False and pos_num == False:
        left = input('Ошибка ввода, введите левую границу диапазона: \n')
    right = input('Отлично, теперь введите правую границу диапазона: \n')
    neg_num = right.startswith('-') and right[1:].isdigit()
    pos_num = right.isdigit()
    flag = True
    while flag:
        while neg_num == False and pos_num == False:
            right = input('Ошибка ввода, введите правую границу диапазона: \n')
        while right <= left:
            right = input('Ошибка ввода, правая граница не может быть меньше или равной левой, введите ещё раз: \n')
        if int(right) > int(left):
            flag = False
    response = input(f'Введите число от {left} до {right}: \n')
    play_self(response, left, right)

def play_self(response, left, right):
    total = 1
    number = r.randint(int(left), int(right))
    while response != str(number):
        if response.startswith('-') and response[1:].isdigit() or response.isdigit():
            if int(response) > int(right):
                response = input(f'''Вы ввели число больше, чем верхняя граница, попробуйте ещё раз:\n''')
            elif int(response) < int(left):
                response = input('''Вы ввели число меньше, чем нижняя граница, попробуйте ещё раз:\n''')
            elif int(response) < number:
                response = input('''Загаданное число больше, попробуйте ещё раз:\n''')
            elif int(response) > number:
                response = input('''Загаданное число меньше, попробуйте ещё раз:\n''')
        else:
            response = input(f'''В вашем ответе должны быть только цифры, попробуйте ещё раз:\n''')
        total += 1
    response2 = input((
        f'''Поздравляем, вы угадали число {number}! Всего было использовано попыток: {total}.  Хотите попробовать ещё раз?(да/нет):\n'''))
    finish(response2)

def play_auto(response):
    total = 1
    number = r.randrange(101)
    while response != str(number):
        if response.startswith('-') and response[1:].isdigit() or response.isdigit():
            if int(response) > 100:
                response = input(f'''Вы ввели число больше, чем верхняя граница, попробуйте ещё раз:\n''')
            elif int(response) < 0:
                response = input('''Вы ввели число меньше, чем нижняя граница, попробуйте ещё раз:\n''')
            elif int(response) < number:
                response = input('''Загаданное число больше, попробуйте ещё раз:\n''')
            elif int(response) > number:
                response = input('''Загаданное число меньше, попробуйте ещё раз:\n''')
        else:
            response = input(f'''В вашем ответе должны быть только цифры, попробуйте ещё раз:\n''')
        total += 1
    response2 = input((
        f'''Поздравляем, вы угадали число {number}! Всего было использовано попыток: {total}.  Хотите попробовать ещё раз?(да/нет):\n'''))
    finish(response2)

def finish(response2):
    if response2.lower() == 'да':
        print('Славно!')
        response = input('Вы сами выберите границы или нам сделать это автоматически?(сам/автоматически): \n')
        flag = True
        while flag:
            if response.lower() == 'автоматически':
                response = input('Попробуйте угадать число от 0 до 100! Ваше число:\n')
                play_auto(response)
                break
            elif response.lower() == 'сам':
                left = input('Введите левую границу диапазона: \n')
                self(left)
                break
            else:
                response = input('Вы ввели неправильную команду, введите ещё раз:\n')
    elif response2.lower() == 'нет':
        print('Спасибо за игру!')
    else:
        finish(input('''Вы ввели неправильную команду, введите ещё раз:\n'''))

start()