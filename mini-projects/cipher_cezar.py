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
                res += encrypt(c, key, cardo, eng_lower_alphabet)
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
                res += decrypt(c, key, cardo, eng_lower_alphabet)
            elif c in eng_upper_alphabet:
                res += decrypt(c, key, cardo, eng_upper_alphabet)
            else:
                res += c
    return res

def calc_key(s):
    # образаем любые не-буквы в начале и в конце слова
    while not (s[0] in eng_lower_alphabet or s[0] in eng_upper_alphabet):
        s = s[1:]
    while not (s[-1] in eng_lower_alphabet or s[-1] in eng_upper_alphabet):
        s = s[:-1]
    return len(s)

def decode():
    s = input('Введите английский текст для расшифровки:')
    lang = 'en'
    direction = 'e'
    for i in range(25):
        print(process(s, direction, lang, i))
    return 0

def ave_cesar():
    """ 
    Аве, Цезарь 🌶️
    На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. 
    Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). 
    Строчные буквы при этом остаются строчными, а прописные – прописными.

    Формат входных данных 
    На вход программе подается строка текста на английском языке.

    Формат выходных данных
    Программа должна вывести зашифрованный текст в соответствии с условием задачи.

    Примечание. Символы, не являющиеся английскими буквами, не изменяются.

    Sample Input 1:
    Day, mice. "Year" is a mistake!
    Sample Output 1:
    Gdb, qmgi. "Ciev" ku b tpzahrl!
    Sample Input 2:
    my name is Python!
    Sample Output 2:
    oa reqi ku Veznut! """

    lang = 'en'
    direction = 'e'
    s = 'Day, mice. "Year" is a mistake!'

    for word in s.split():
        print(process(word, direction, lang, calc_key(word)), end=' ')
    return 0

# main
lang = get_lang()
direction = get_direction()
key = get_key()
s = input('Введите текст:')

print(process(s, direction, lang, key))