'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
r = int(t[1])
t = [int(x) for x in input().split()]
temp = sum(t)
print(abs(temp) // r + (0 if abs(temp) % r == 0 else 1))