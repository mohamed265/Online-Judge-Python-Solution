'''
Created on Feb 13, 2015

@author: mohamed265
'''
n = int(input())
temp = [int(x) for x in input().split()]
slon = 9999999999999999
for i in range(n):
    temp2 = [int(x) for x in input().split()]
    t = 0
    for j in range(temp[i]):
        t += temp2[j] * 5
        t += 15
    slon = min(slon , t)
print(slon)