# объявление функции
def get_days(month):
    if month == 2:
        return 28
    elif ((month % 2 == 1 and month < 8) or
          (month % 2 == 0 and month >= 8)):
        return 31
    else:
        return 30

# считываем данные
#num = int(input())

# вызываем функцию
[print(num, get_days(num)) for num in range(1, 13)]