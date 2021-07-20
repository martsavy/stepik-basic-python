from datetime import datetime
import math
start = datetime.now().time()
#for e in range(1, 151):
#    print(e)
#    e1 = e ** 5
#    for a in range(1, e + 1):
for a in range(1, 151):
    print(a)
    a1 = a ** 5
    for b in range(1, a + 1):
        b1 = b **5
        for c in range(1, b + 1):
            c1 = c ** 5
            for d in range(1, c + 1):
                val1 = (a1 + b1 + c1 + d ** 5)
                val2 =  val1 ** (1.0 / 5)
                val3 = int(val2 + 0.5)
                val4 = val3 ** 5
                if (val1 == val4):
                    print(a, b, c, d, (a1 + b1 + c1 + d ** 5) ** (1 / 5))
                    print('Sum =', a + b + c + d + (a1 + b1 + c1 + d ** 5) ** (1 / 5))
print('start= ', start)
print('finish=', datetime.now().time())
# try1
# start= 14:20:59.780723
# finish= 14:48:52.043073
# try2
# start=  15:59:41.813889
# finish= 16:05:34.386633
# 144
# 133 110 84 27  = 144
# start=  11:14:48.065966
# finish= 11:15:06.978396