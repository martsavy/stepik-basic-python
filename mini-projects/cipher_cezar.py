eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabets = eng_lower_alphabet + eng_upper_alphabet + rus_lower_alphabet + rus_upper_alphabet

def encrypt(char, key, cardo, alphabet):
    # зашифровка символа-аргумента. Возврат зашифрованного символа
    return alphabet[((alphabet.find(char) + key) % cardo)]
def decrypt(char, key, cardo, alphabet):
    # дешифровка символа-аргумента. Возврат дешифрованного символа
    return alphabet[((alphabet.find(char) - key) % cardo)]

def get_lang(): 
    # ввод языка и проверка введённого значения (должно быть en или ru)
    lang = input("Язык алфавита русский или английский? [ru/en]")
    while True:
        if lang == 'ru' or lang == 'en':
            return lang
        else:
            lang = input("Нужно ввести 'ru' или 'en':")

def get_direction():
    # ввод направления (шифровка/дешифровка) и проверка введённого значения (должно быть e или d)
    direction = input("Введите направление: шифрование или дешифрование; [encrypt=e/decrypt=d]")
    while True:
        if direction == 'e' or direction == 'd':
            return direction
        else:
            direction = input("Нужно ввести 'e' или 'd':")

def get_key():
    # ввод сдвига и проверка введённого значения (должно целое число)
    key = input("Введите шаг сдвига (со сдвигом вправо):")
    while True:
        if key.isdigit:
            return int(key)
        else:
            key = input("Нужно ввести целое число:")

def process(s, direction, lang, key):
    # установка мощности алфавита
    if lang == 'ru':
        cardo = 32
    else:
        cardo = 26
    res = ''
    for c in s:
        if direction == 'e':
            if c in rus_lower_alphabet:
                res += encrypt(c, key, cardo, rus_lower_alphabet)
            elif c in rus_upper_alphabet:
                res += encrypt(c, key, cardo, rus_upper_alphabet)
            elif c in eng_lower_alphabet:
                res += encrypt(c, key, cardo, rus_lower_alphabet)
            elif c in eng_upper_alphabet:
                res += encrypt(c, key, cardo, eng_upper_alphabet)
            else:
                res += c
        if direction == 'd':
            if c in rus_lower_alphabet:
                res += decrypt(c, key, cardo, rus_lower_alphabet)
            elif c in rus_upper_alphabet:
                res += decrypt(c, key, cardo, rus_upper_alphabet)
            elif c in eng_lower_alphabet:
                res += decrypt(c, key, cardo, rus_lower_alphabet)
            elif c in eng_upper_alphabet:
                res += decrypt(c, key, cardo, eng_upper_alphabet)
            else:
                res += c
    return res

# main
lang = get_lang()
direction = get_direction()
key = get_key()
s = input('Введите текст:')

print(process(s, direction, lang, key))
