'''
Created on ١٣‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
x = int(t[1])
t = [int(x) for x in input().split()]
t.sort()
slon  = 0
for i in range(n):
    slon += t[i] * x
    x = (x-1) or 1
print(slon)