def encrypt(char, key, cardo):
    pass
def decrypt(char, key, cardo):
    pass
def get_lang():
    lang = input("Язык алфавита русский или английский? [ru/en]")
    while True:
        if lang == 'ru' or lang == 'en':
            return lang
        else:
            lang = input("Нужно ввести 'ru' или 'en':")

def get_direction():
    direction = input("Введите направление: шифрование или дешифрование; [encrypt=e/decrypt=d]")
    while True:
        if direction == 'e' or direction == 'd':
            return direction
        else:
            direction = input("Нужно ввести 'e' или 'd':")
def get_key():
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
