# объявление функции
def print_digit_sum(num):
    li = [0] * len(str(num))
    li.extend(str)
    li = [int(i) for i in str(num).split('')]
    print(li)
    print(sum(li))

# считываем данные
#n = int(input())
n = 12345
# вызываем функцию
print_digit_sum(n)