for b in range(1, 11):
    for c in range(1, 21):
        for t in range(1, 201):
            if (b * 10 + c * 5 + t * 0.5 == 100) \
                and b + c + t == 100:
                print('b =', b, 'c =', c, 't =', t)