'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
r = int(t[0])
c = int(t[1])
slon = 0
t = []
for i in range(r):
    temp = input()
    if temp.count('S') == 0:
        slon += c
    t.append(temp)
k = slon // c
#print(k , slon)
for i in range(c):
    temp = 0
    for j in range(r):
        if t[j][i] == 'S':
            temp += 1
    if temp == 0:
        slon += (r - k)
print (slon)
