# объявление функции
# возвращает True если число простое и False если нет. Простое число - это число, которое делится только на 1 и самого себя без остатка.
def is_prime(num):
    flag = True
    if num == 1:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            flag = False
    return flag

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))