""" Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку
 в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:

this_is_camel_cased
is_prime_number """

# объявление функции
def convert_to_python_case(text):
    res = text[0:1].lower()
    
    for c in text[1:]:
        if c.isupper():
            res = res + '_' + c.lower()
        else:
            res += c
    return res

# проверка
print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))