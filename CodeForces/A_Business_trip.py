'''
Created on ٠٨‏/١٢‏/٢٠١٤

@author: mohamed265
'''
k = int (input())
lis = [int(x) for x in input().split()]
lis.sort(reverse=True)
su = slon = 0
flag = True
for i  in range(12) :
    if su >= k:
        print(slon)
        flag = False
        break
    else:
        slon += 1
        su += lis[i]
        if su >= k:
            print(slon)
            flag = False
            break
if flag :
    print(-1)