# put your python code here
s = input()
num = [int(a) for a in s.split()]
print(num)
mi = min(num)
ma = max(num)
i_max = num.index(max(num))
i_min = num.index(min(num))
num.insert(i_min, max(num))
print(num)
del num[i_min + 1]
print(num)
num.insert(i_max, mi)
del num[i_max + 1]
print(*num, sep=' ')