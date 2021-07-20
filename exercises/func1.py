# объявление функции
def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*', ' ' * 8, '*', sep='')
    print('*' * 10)

# основная программа
draw_box()  # вызов функции
# объявление функции
def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

# основная программа
draw_triangle()  # вызов функции