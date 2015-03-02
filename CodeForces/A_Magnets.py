'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
cha = ''
slon = 0
n = int(input())
for i in range(n):
    t = input()
    if t[1] != cha:
        slon += 1
        cha = t[1]
print(slon)
