'''
Created on Jan 5, 2015

@author: mohamed265
'''
n = int(input())
map = {}
for i in range(n):
    t = input()
    if map.__contains__(t):
        print(t,map[t],sep='')
        map[t] += 1
    else:
        print("OK")
        map[t] =1