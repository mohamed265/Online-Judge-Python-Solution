'''
Created on ١١‏/١٢‏/٢٠١٤

@author: mohamed265
'''
 
def fun(t , i , j , temp):
    for k in range(i, j + 1):
        temp += -1 if 1 - t[k] == 0 else 1
    # print(t)
    return temp

n = int(input())
t = [int(x) for x in input().split()]
slon = -100 
temp = t.count(1)
# if temp == len(t):
#    print(0)
# else:  
for i in range(n):
    # if t[i] == 0:
    for j in range(i , n):
        slon = max(slon , fun(t, i , j , temp))
print(slon)
