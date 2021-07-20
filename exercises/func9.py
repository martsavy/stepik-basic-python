""" Ровно в одном:
Напишите функцию is_one_away(word1, word2), 
которая принимает в качестве аргументов два слова word1 и word2 и 
возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и 
False в противном случае. """

# объявление функции
def is_one_away(word1, word2):
    flag1 = False
    flag2 = False
    if len(word1) == len(word2):
        flag1 = True
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            flag2 = True
    return all([flag1, flag2])
    
print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
print(is_one_away('bike', 'bike'))

""" должен выводить:
True
True
False
False 
False """


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

