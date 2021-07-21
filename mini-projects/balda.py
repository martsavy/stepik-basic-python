from random import choice
words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", 
                "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", 
                "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]
# функция получения случайного слова из словаря (все буквы в верхнем регистре)
def get_word():
    return choice(words_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = ['_'] * len(word)# список, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')

    while tries > 0:
        print(f'Уже вводили буквы:{guessed_letters}')
        print(f'Уже вводили слова:{guessed_words}')
        print(display_hangman(tries))
        print(*word_completion)
        s = input().upper()
        if not s.isalpha():
            continue
        if s in guessed_letters or s in guessed_words:
            t = input('Вы уже вводили эту букву/слово. Нажмите Enter, чтобы продолжить')
            continue
        if len(s) == 1:
            if s in word:
                guessed_letters.append(s)
                for i in range(len(word)):
                    if word[i] == s:
                        word_completion[i] = s
                continue
            else:
                tries -= 1
                guessed_letters.append(s)
                continue
        if s == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            break
        else:
            guessed_words.append(s)
            tries -= 1
            continue
        tries -= 1
    if tries == 0:
        display_hangman(tries)
        print(f'Загаданное слово:{word}')

play(get_word())