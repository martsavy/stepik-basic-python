from random import choice
def request_count():
    print('Сколько паролей нужно сгенерировать? Введите цифру: ', end='')
    while True:
        count = input()
        if count.isdigit():
            return int(length)
        else:
            print('Вы должны ввести число!')

def request_len():
    # бесконечный цикл, пока не введена длина пароля > 7
    while True:
        length = input('Введите длину пароля (> 7): ')
        if length.isdigit():
            if int(length) > 7:
                return int(length)
        else:
            print('Вы должны ввести число > 7 !')

def gen_chars(is_low_letters, is_hi_letters, is_numbers, is_specials, is_exclude):
    # строки букв, цифр и символов
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    
    # добавляем к общему списку для генерации пароля только те, которые захотел пользователь
    # на основании ответов на вопросы (в функцию передаются булевские значения)
    if is_low_letters:
        chars += lowercase_letters
    if is_hi_letters:
        chars += uppercase_letters
    if is_numbers:
        chars += digits
    if is_specials:
        chars += punctuation
    if is_exclude:
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    return chars
    
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password


print('Приветствую вас в генераторе паролей!')

length = request_len()

is_numbers = input('Включать ли цифры 0123456789? [y/n] ').lower() == 'y'
is_hi_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? [y/n] ').lower() == 'y'
is_low_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? [y/n] ').lower() == 'y'
is_specials = input('Включать ли символы !#$%&*+-=?@^_? [y/n] ').lower() == 'y'
is_exclude = input('Исключать ли неоднозначные символы "il1Lo0O" [y/n] ') == 'y'

for _ in range(request_count()):
    chars = gen_chars(is_low_letters, is_hi_letters, is_numbers, is_specials, is_exclude)
    password = generate_password(length, chars)
    print('Ваш пароль:', password)
