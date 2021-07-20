# объявление функции
def is_password_good(password):
    flag = False
    flag_d = False
    for c in password:
        if c.isdigit():
            flag_d = True
    if (len(password) > 7 and
       password.lower() != password and
       password.upper() != password and
       flag_d):
        flag = True
    return flag    

def is_password_good_list_all(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])



# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
print(is_password_good_list_all(txt))