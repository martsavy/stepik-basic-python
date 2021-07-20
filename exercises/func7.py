# put your python code here
def quick_merge(list1):
    res = []
    for i in range(len(list1)):
        res = res + [int(a) for a in list1[i].split()]
    res.sort()
    return res
def quick_merge_pop(list1):
    res = []
    for i in range(len(list1)):
        res_temp = []
        list1_i = [int(j) for j in list1[i].split()]
        while res and list1_i:
            if res[0] < list1_i[0]:
                res_temp.append(res.pop(0))
            else:
                res_temp.append(list1_i.pop(0))
        if len(res) == 0:
            res_temp.extend(list1_i)
        if len(list1_i) == 0:
            res_temp.extend(res)
        res = res_temp
    return res
n = int(input())
list1 = [0] * n
for i in range(n):
    list1[i] = input()
print(quick_merge(list1))
print(quick_merge_pop(list1))
