# объявление функции
def find_all(target, symbol):
    result = []
    if target.find(symbol) == -1:
        return result
    i = 0
    while target[i:].find(symbol) >= 0:
        result.append(i + target[i:].find(symbol))
        i = i + target[i:].find(symbol) + 1
    return result

# считываем данные
#s = input()
#char = input()

# вызываем функцию
print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))