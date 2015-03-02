'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''


n = int(input())
lis = []
for i in range(n):
    t = [int(x) for x in input().split()]
    lis.append(t)
flag = True
for i in range(3):
    sum = 0
    for j in range(n):
        sum += lis[j][i]
    if sum != 0:
        flag = False
print("YES") if flag else print("NO")
        