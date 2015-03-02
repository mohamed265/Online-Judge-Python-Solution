'''
Created on ٠٧‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[1])
m = int(t[0])
slon = 0
lis = [int(x) for x in input().split()]
current = 1
for x in lis:
    if current <= x:
        slon += (x - current)
        current = x
    else :
        slon += (m - current) + (x)
        current = x
print(slon)
