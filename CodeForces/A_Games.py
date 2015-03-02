'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
lis = []
for i in range(n):
    lis.append(input().split())
#print(lis)
slon = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if lis[i][0] == lis[j][1]:
                slon += 1
print(slon)
    