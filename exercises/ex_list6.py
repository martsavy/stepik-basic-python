# put your python code here
#12
# print("Введите своё имя")
# name = input()
# print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
# password = input()
# if password == "hoover":
#     print("Здравствуйте, рыцарь", name)         #долой Макнамару
# elif password == "noncr":
#     print("Здравствуйте, паладин", name)
# elif password == "gelios":
#     print("Здравствуйте, старейшина", name)          #Элайджа вперёд
# else:
#     print("Здравствуйте, послушник", name)
s = input()
n = int(s[1:])
for _ in range(n):
    s = input()
    if "#" in s:
        s = s[:s.find('#')]
    s = s.rstrip()
    print(s)