# объявление функции
def merge(list1, list2):
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    #res = [0] * (n + m)
    res = []
    while i < n or j < m:
        if i < n:
            if j < m:
                if list1[i] < list2[j]:
                    res.append(list1[i])
                    i += 1
                else:
                    res.append(list2[j])
                    j += 1
            else:
                res.append(list1[i])
                i += 1
        else:
            res.append(list2[j])
            j += 1
    return res

# вызываем функцию
print(merge([5, 6, 7, 8], [1, 2, 3]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))