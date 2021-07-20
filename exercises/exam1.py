#n = int(input())
n = 255
count_3 = 0
count_last = 0
last = n % 10
count_even = 0
sum_more_5 = 0
composition_more_7 = 1
count_0_and_5 = 0
while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        count_3 += 1
    if last_digit == last:
        count_last +=1
    if last_digit % 2 == 0:
        count_even += 1
    if last_digit > 5:
        sum_more_5 += last_digit
    if last_digit > 7:
        composition_more_7 *= last_digit
    if last_digit == 5 or last_digit == 0:
        count_0_and_5 += 1
    n //= 10
print(count_3, count_last, count_even, sum_more_5, composition_more_7, count_0_and_5, sep='\n')