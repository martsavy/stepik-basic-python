from random import randint
def is_valid(a):
    if not a.isdigit():
        return False
    if 1 <= int(a) <= 100:
        return True
    else:
        return False
n = randint(1, 100)
count = 0
print('Добро пожаловать в числовую угадайку')
while True:
    print('Введите число от 1 до 100')
    answer = input()
    count += 1
    if not is_valid(answer):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    int_answer = int(answer)
    if int_answer > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    elif int_answer < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали, поздравляем!')
        print(f'Количество попыток: {count}')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
