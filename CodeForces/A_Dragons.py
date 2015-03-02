'''
Created on ٠٧‏/١٢‏/٢٠١٤

@author: mohamed265
'''
lis = []
t = input().split()
s = int(t[0])
n = int(t[1])
for i in range(n):
    lis.append([int(x) for x in input().split()])
lis.sort()
flag = True
for i in range(n):
    if s > lis[i][0]:
        s += lis[i][1]
    else:
        flag = False
        break
print("YES") if flag else print("NO")
