'''
Created on Feb 24, 2015

@author: mohamed265
'''
temp = input().split()
n = int(temp[0])
p = float(temp[1])
t = int(temp[2])
slon = 0
for i in range(t):
    slon += (p/(i+1)) * (n)
print(slon)