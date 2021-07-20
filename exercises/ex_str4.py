# put your python code here
# s = input()
s = 'abch12345h'
print(s.find('h') +1)
print(s.rfind('h'))
s1 =  s[s.find('h') + 1:s.rfind('h')]
print(s1[::-1])
res = s[:s.find('h')] + s[s.find('h'):s.rfind('h'):-1] + s[s.rfind('h'):]
print(res)

a=int(s.find('h'))
b=int(s.rfind('h'))
print(s[:a]+s[b:a:-1]+s[b:])

print(s[9:3:-1])