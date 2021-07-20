from random import randint
def is_valid(a, rrange):
    if not a.isdigit():
        return False
    if 1 <= int(a) <= rrange:
        return True
    else:
        return False
def body(rrange):
    n = randint(1, rrange)
    count = 0
    while True:
        print(f'Введите число от 1 до {rrange}')
        answer = input()
        count += 1
        if not is_valid(answer, rrange):
            print(f'А может быть все-таки введем целое число от 1 до {rrange}?')
            continue
        int_answer = int(answer)
        if int_answer > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif int_answer < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток: {count}')
            break

print('Добро пожаловать в числовую угадайку')
print('Введите правую границу (1..Х)')
while True:
    rrange = input()
    if not rrange.isdigit():
        print('А может быть все-таки введем целое число?')
    else:
        break

body(int(rrange))
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
