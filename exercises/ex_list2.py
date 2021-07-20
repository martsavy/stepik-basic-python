# put your python code here
# input n numbers, then print first negative, then zero, then positive
l = [int(input()) for _ in range(int(input()))]
print(*[c for c in l if c < 0], sep='\n')
print(*[c for c in l if c == 0], sep='\n')
print(*[c for c in l if c > 0], sep ='\n')