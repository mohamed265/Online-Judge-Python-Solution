'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
m = int(t[1])
slon = 0
for a in range(1001):
    for b in range(1001):
        if a ** 2 + b == n and a + b ** 2 == m:
            slon += 1
print(slon)
