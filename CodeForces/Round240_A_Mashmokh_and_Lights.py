'''
Created on Jan 28, 2015

@author: mohamed265
'''
t = input().split()
n = int(t[0])
m = int(t[1])
t = [int(x) for x in input().split()]
slon = [0 for x in range(n)]
for i in range(m):
    for j in range(t[i], n + 1):
        if j != 0 and slon[j - 1] == 0:
            slon[j - 1] = t[i]
print(*slon)
