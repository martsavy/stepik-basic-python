""" BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и
 возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False """

# объявление функции
def is_prime(num):
    flag = True
    if num == 1:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            flag = False
    return flag

def is_valid_password(password):
    flag1 = False
    flag2 = False
    flag3 = False
    list1 = [int(i) for i in password.split(':')]
    if len(list1) != 3:
        return False
    if str(list1[0]) == str(list1[0])[::-1]:
        flag1 = True
    if is_prime(list1[1]):
        flag2 = True
    if list1[2] % 2 == 0:
        flag3 = True
    return all([flag1, flag2, flag3])


# проверка
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))