'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
m = [input().split() , input().split(), input().split(), input().split(), input().split()]
slon = 0
for j in range(5):
    for i in range(5):
        if m[j][i] == '1':
            slon = abs(i-2) + abs(j-2)
print(slon)
