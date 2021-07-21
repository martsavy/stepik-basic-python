def encrypt(char, key, cardo):
    pass
def decrypt(char, key, cardo):
    pass

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
# main
lang = get_lang()
direction = get_direction()
key = get_key()
