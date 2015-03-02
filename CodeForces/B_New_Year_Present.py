'''
Created on ١١‏/١٢‏/٢٠١٤

@author: mohamed265
'''

n = int(input())
target = [int(x) for x in input().split()]
slon = ""
'''
temp = []
slon = ""
for i in range(n):
    temp.append(0)
    '''
for i in range(n - 1):
    slon += ('PRL' * (target[i] - 1)) + ('R' if target[i] == 0 else 'PR')
    
slon += ('PLR' * (target[n - 1] - 1)) + ('' if target[n - 1] == 0 else 'P')
print(slon)
