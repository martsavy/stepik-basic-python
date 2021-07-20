# put your python code here
base = [input() for _ in range(int(input()))]
k = int(input())
find = [input() for _ in range(k)]
for s in base:
    count = 0
    for st in find:
        if s.casefold() in st.casefold():
            count += 1
    if count == k:
        print(s)