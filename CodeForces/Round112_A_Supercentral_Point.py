'''
Created on Jan 6, 2015

@author: mohamed265
'''
n = int(input())
list = []
for i in range(n):
    list.append([int(x) for x in input().split()])
    #list.append(input().split())
slon = 0
t1 = t2 = t3 = t4 = 0
for i in range(n):
    #print(list[i])
    t1 = t2 = t3 = t4 = 0
    for j in range(n):
        if i != j:
            if list[i][0] > list[j][0] and list[i][1] == list[j][1]:
                t1 += 1
            if list[i][0] < list[j][0] and list[i][1] == list[j][1]:
                t2 += 1
            if list[i][0] == list[j][0] and list[i][1] > list[j][1]:
                t3 += 1
            if list[i][0] == list[j][0] and list[i][1] < list[j][1]:
                t4 += 1
    #print(t1,t2,t3,t4)
    if t1 > 0 and t2 > 0 and t3 > 0 and t4 > 0:
        slon += 1
print(slon)