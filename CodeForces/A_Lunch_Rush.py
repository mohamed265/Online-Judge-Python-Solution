'''
Created on ١٠‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
k = int(t[1])
slon = -100000000000000
for i in range(n):
    t = input().split()
    if int(t[1]) > k:
        slon = max(slon, int(t[0]) - (int(t[1]) - k))
    else:
        slon = max(slon, int(t[0]))
    
print(slon)
