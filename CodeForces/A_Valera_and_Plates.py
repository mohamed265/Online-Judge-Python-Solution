'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''

t = input().split()
m = int(t[1])
k = int(t[2])
s = input()
p = s.count('1')
b = s.count('2')
m -= p
k -= b
#print(m , k)
if m > 0:
    k += m
    if k < 0:
        print(abs(k))
    else:
        print(0)
elif k >= 0:
    print(abs(m))
else:
    print(abs(k) + abs(m))
