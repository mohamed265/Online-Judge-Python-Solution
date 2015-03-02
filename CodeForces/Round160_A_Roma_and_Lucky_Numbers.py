'''
Created on Jan 28, 2015

@author: mohamed265
'''
t = input().split()
n = int(t[0])
k = int(t[1])
t = input().split()
slon = temp = 0
for i in range(len(t)):
    temp = t[i].count('4') + t[i].count('7')
    if temp <= k:
        slon += 1
print(slon)
