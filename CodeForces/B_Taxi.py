'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = input()
m = input()
slon = m.count('4')
a, b, c = m.count('1'), m.count('2'), m.count('3')
slon += b // 2 + c
if b % 2 == 1:
    slon += 1
    a -= 2
a -= c
if a > 0 :
    slon += a // 4
    if a % 4 != 0:
        slon += 1
print(slon)
