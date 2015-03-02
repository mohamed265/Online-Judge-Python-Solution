'''
Created on ٠٧‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
t = [int(x) for x in input().split()]
slon = 0
off = 0
for x in t:
    if x == -1 and off == 0:
        slon += 1
    elif x == -1 and off > 0:
        off -= 1
    else:
        off += x
print(slon)
