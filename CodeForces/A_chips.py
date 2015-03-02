'''
Created on ١٣‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
m = int(t[1])
totalN = (n / 2) * n + n / 2
#print(totalN)
rem = m - totalN * (m // totalN)
for i in range(1, n + 1):
    if rem >= i:
        rem -= i
    else:
        break
print(int(rem))
