'''
Created on ١٠‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int (t[0])
mo = int(t[1])
lis = []
for i in range(n):
    t = input().split()
    flag = False
    for j in range(int(t[0])):
        if mo > int(t[j + 1]):
            flag = True
    if flag:
        lis.append(i + 1)
        # print(i+1,end = ' ')
print(len(lis))
for i in range(len(lis)):
    print(lis[i] , end=' ')
