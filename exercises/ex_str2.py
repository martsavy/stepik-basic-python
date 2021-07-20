# put your python code here
#s = input()
s = "aaAAAbbV123"
c = 0
l = ''
for i in range(0, len(s)):
    if s.count(s[i]) >= c:
        l = s[i]
        c = s.count(s[i])
print(l)