print('Привет, это программа "Шифр Цезаря" и я могу помочь тебе зашифровать или расшифровать шифр!')

def start():
    response = input('Чем я могу быть полезен?(зашифровать/расшифровать)\n').lower()
    while response != 'зашифровать' and response != 'расшифровать':
        response = input('Ошибка ввода. Чем я могу быть полезен?(зашифровать/расшифровать)\n').lower()
    response2 = input('На каком языке будет текст?(англ/рус)\n').lower()
    while response2 != 'англ' and response2 != 'рус':
        response2 = input('Ошибка ввода. На каком языке будет текст?(англ/рус)\n').lower()
    if response == 'зашифровать' and response2 == 'рус':
        encrypt_ru()
    elif response == 'зашифровать' and response2 == 'англ':
        encrypt_eng()
    elif response == 'расшифровать' and response2 == 'англ':
        decrypt_eng()
    else:
        decrypt_ru()

def encrypt_eng():
    encrypt_text = ''
    response = input('На сколько букв сдвигаем вправо?(число)\n')
    while response.isdigit() == False:
        response = input('Ошибка ввода. На сколько букв сдвигаем вправо?(число)\n')
    response_int = int(response)
    text = input('Введите текст: \n')
    for i in range(len(text)):
        if ord('A') <= ord(text[i]) <= ord('Z'):
            total = ord(text[i]) + response_int
            while total > ord('Z'):
                total = ord('A') + (total - ord('Z')) -1
            encrypt_text += chr(total)
        elif ord('a') <= ord(text[i]) <= ord('z'):
            total = ord(text[i]) + response_int
            while total > ord('z'):
                total = ord('a') + (total - ord('z')) -1
            encrypt_text += chr(total)
        else:
            encrypt_text += text[i]
    print(f'Итог:\n{encrypt_text}')
    reply()

def encrypt_ru():
    encrypt_text = ''
    response = input('На сколько букв сдвигаем вправо?(число)\n')
    while response.isdigit() == False:
        response = input('Ошибка ввода. На сколько букв сдвигаем вправо?(число)\n')
    response_int = int(response)
    text = input('Введите текст: \n')
    for i in range(len(text)):
        if ord('а') <= ord(text[i]) <= ord('я'):
            total = ord(text[i]) + response_int
            while total > ord('я'):
                total = ord('а') + (total - ord('я')) -1
            encrypt_text += chr(total)
        elif ord('А') <= ord(text[i]) <= ord('Я'):
            total = ord(text[i]) + response_int
            while total > ord('Я'):
                total = ord('Я') + (total - ord('Я')) -1
            encrypt_text += chr(total)
        else:
            encrypt_text += text[i]
    print(f'Итог:\n{encrypt_text}')
    reply()

def decrypt_eng():
    decrypt_text = ''
    response = input('На сколько букв сдвигаем влево?(число)\n')
    while response.isdigit() == False:
        response = input('Ошибка ввода. На сколько букв сдвигаем влево?(число)\n')
    response_int = int(response)
    text = input('Введите текст: \n')
    for i in range(len(text)):
        if ord('A') <= ord(text[i]) <= ord('Z'):
            total = ord(text[i]) - response_int
            while total < ord('A'):
                total = ord('Z') - (ord('A') - total ) -1
            decrypt_text += chr(total)
        elif ord('a') <= ord(text[i]) <= ord('z'):
            total = ord(text[i]) - response_int
            while total < ord('a'):
                total = ord('z') - (ord('a') - total ) -1
            decrypt_text += chr(total)
        else:
            decrypt_text += text[i]
    print(f'Итог:\n{decrypt_text}')
    reply()

def decrypt_ru():
    decrypt_text = ''
    response = input('На сколько букв сдвигаем влево?(число)\n')
    while response.isdigit() == False:
        response = input('Ошибка ввода. На сколько букв сдвигаем влево?(число)\n')
    response_int = int(response)
    text = input('Введите текст: \n')
    for i in range(len(text)):
        if ord('А') <= ord(text[i]) <= ord('Я'):
            total = ord(text[i]) - response_int
            while total < ord('А'):
                total = ord('Я') - (ord('А') - total ) -1
            decrypt_text += chr(total)
        elif ord('а') <= ord(text[i]) <= ord('я'):
            total = ord(text[i]) - response_int
            while total < ord('а'):
                total = ord('я') - (ord('а') - total ) -1
            decrypt_text += chr(total)
        else:
            decrypt_text += text[i]
    print(f'Итог:\n{decrypt_text}')
    reply()

def reply():
    response = input('Хотите ли вы ещё воспользоваться моими услугами?(да/нет)\n').lower()
    while response != 'да' and response != 'нет':
        response = input('Ошибка ввода. Хотите ли вы ещё воспользоваться моими услугами?(да/нет)\n')
    if response == 'да':
        start()
    else:
        end()

def end():
    print('Всего хорошего!')

start()