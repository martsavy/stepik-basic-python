for i in range(10):
    print(i, end='*')
    if i > 6:
        break
p = 1
count = 0
for i in range(10):
    x = int(input())
    if x > 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')