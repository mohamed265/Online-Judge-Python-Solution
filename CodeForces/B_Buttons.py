'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''
co = n = int(input())
slon = 0#1 if n % 2 == 0 else -1 
for i in range(1, co+1):
    slon += n * i - (co-n)
    n -= 1
print(slon)
