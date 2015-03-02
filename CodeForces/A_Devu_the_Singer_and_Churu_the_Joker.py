'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
mi = int(t[1])
t = [int(x) for x in input().split()]
t = sum(t)
if t + (n - 1) * 10 > mi:
    print(-1)
else:
    slon = (n - 1) * 2
    slon += ((mi - (t + (n - 1) * 10) ) // 5) 
    print(slon)
