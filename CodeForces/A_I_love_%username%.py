'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
lis =  [ int(x) for x in input().split()]
ma = mi = lis[0]
slon = 0
for i in range(1, n):
    if lis[i] > ma:
        ma = lis[i]
        slon += 1
    elif lis[i] < mi:
        mi = lis[i]
        slon += 1
print(slon)
