import random as r
'''Создаю списки с символами, буквами и цифрами'''
digits = []
lowercase_letters = []
uppercase_letters = []
punctuation_char = '!#$%&*+-=?@^_'
punctuation = []
exception = 'il1Lo0O'

for i in range(10):
    digits.append(str(i))
for i in range(97, 123):
    lowercase_letters.append(chr(i))
for i in range(65, 91):
    uppercase_letters.append(chr(i))
for i in punctuation_char:
    punctuation.append(i)

'''Приветствие и начало программы'''
response = input('Привет, меня зовут ГБП (Генератор Безопасных Паролей). Нужен ли тебе пароль?(да/нет)\n').lower()

'''Если пользователю нужен пароль - идут функции по очереди, если не нужен - программа закрывается'''
def start(response):
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'да':
        question_quantity()
    else:
        end()

'''Запрашивается количество паролей'''
def question_quantity():
    global quantity
    response = input('Сколько вам нужно паролей?(число)\n')
    while response.isdigit() == False:
        response = input('Ошибка ввода. Сколько вам нужно паролей?(число)\n')
    if int(response) == 0:
        end()
    else:
        quantity = int(response)
    question_length()

'''Запрашивается длина пароля'''
def question_length():
    global length
    response = input('Какая необходимая длина пароля?(число, минимум 2 символа)\n')
    while response.isdigit() == False:
        response = input('Ошибка ввода. Какая необходимая длина пароля?(число, минимум 2 символа)\n')
    if int(response) < 2:
        print('Ошибка ввода. Вы ввели значение меньше 2')
        question_length()
    else:
        length = int(response)
        question_digits()

'''Запрашивается разрешение на добавление цифр'''
def question_digits():
    case = []
    response = input('Включать ли цифры? (пример: 123) (да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'да':
        case.append(digits)
    question_lowercase_letters(case)

'''Запрашивается разрешение на добавление строчных букв'''
def question_lowercase_letters(case):
    response = input('Включать ли строчные (маленькие) буквы? (пример: abc) (да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'да':
        case.append(lowercase_letters)
    question_uppercase_letters(case)

'''Запрашивается разрешение на добавление заглавных букв'''
def question_uppercase_letters(case):
    response = input('Включать ли заглавные (большие) буквы? (пример: ABC) (да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'да':
        case.append(uppercase_letters)
    question_punctuation(case)

'''Запрашивается разрешение на добавление стимволов'''
def question_punctuation(case):
    response = input('Включать ли символы? (пример: $%&-) (да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'да':
        case.append(punctuation)
    if len(case) == 0:
        print('Вы не выбрали никаких символов, начните пожалуйста заново')
        question_quantity()
    else:
        question_exception(case)
'''Если пользователь не выбрал ни одного варианта, то функция возвращает пользователя в самое начало функций,
для повторного прохождения'''

'''Запрашивается разрешение на удаление символов, которые похожи друг на друга'''
def question_exception(case):
    response = input('Исключать ли неоднозначные символы il1Lo0O?(да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'да':
        for l in case:
            n = len(l)
            for c in range(len(l)):
                if l[c] not in exception:
                    l.append(l[c])
            del l[:n]
    gbp(case)

'''Генерируются пароли'''
def gbp(case):
    for i in range(quantity):
        chars = ''
        for j in range(length):
            chars += r.choice(r.choice(case))
        print(chars)
    reply(case)

'''Функция спрашивает у пользователя, нужны ли ему ещё пароли.
Если пароли нужны, то даётся выбор, сгенерировать пароли по
старым параметрам или пользователь введёт новые параметры.
Если пароли больше не нужны - программа закрывается'''

def reply(case):
    response = input('Нужны ли вам ещё пароли? (да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода, введите да или нет:\n')
    if response == 'нет':
        end()
    else:
        response = input('Будем использовать повторно параметры или же вы хотите указать новые?(да - повторно/ нет - новые)\n').lower()
        while response != 'да' and response != 'нет':
            response = input('Ошибка ввода, введите да или нет:\n')
        if response == 'да':
            gbp(case)
        else:
            question_quantity()

def end():
    print('Всего хорошего!')
    
start(response)