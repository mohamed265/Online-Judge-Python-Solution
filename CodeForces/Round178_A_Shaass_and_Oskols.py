'''
Created on Jan 26, 2015

@author: mohamed265
'''
n = int(input())
lis = [int(x) for x in input().split()]
m = int(input())
for i in range(m):
    t = input().split()
    t[0] = int(t[0]) -1
    t[1] = int(t[1])
    if t[0] - 1 >= 0:
        lis[t[0] - 1] += t[1] - 1
    #print(t[0] + 1 , n,t[1]+1<n)
    if t[0] + 1 < n:
        #print(lis[t[0]] - t[1])
        lis[t[0] + 1] += lis[t[0]] - t[1]
    lis[t[0]] = 0
print(*lis,sep = '\n')
