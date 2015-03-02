'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = input()
s = input()
slon = 0
cha = ''
for x in s:
    if x == cha:
        slon += 1
    else:
        cha = x
print(slon)