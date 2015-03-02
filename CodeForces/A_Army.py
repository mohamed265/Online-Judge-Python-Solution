'''
Created on ١٢‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
t = [int(x) for x in input().split()]
s = input().split()
a = int(s[0])
b = int(s[1])
slon = 0
for i in range(a-1,b-1):
    slon += t[i]
print(slon)