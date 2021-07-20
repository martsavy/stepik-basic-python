n = 100500
for i in range(1, n):
    count = 0 
    r = int(i ** (1.0 / 3))
    for j in range(1, r + 1):
        for k in range(j, r + 1):
            if j ** 3 + k ** 3 == i:
                count += 1
    if count == 2:
        print(i)
