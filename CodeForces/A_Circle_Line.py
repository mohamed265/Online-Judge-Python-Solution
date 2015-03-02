'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
lis = [int(x) for x in input().split()]
temp =  input().split()
ttt = tt = t = int(temp[0])
sss = ss = s = int(temp[1])
len1 = len2 = 0
while tt != ss:
    len1 += lis[tt - 1]
    tt += 1
    if tt == n+1:
        tt = 1
        
while ttt != sss:
    len2 += lis[ttt - 2]
    ttt -= 1
    if ttt == 0:
        ttt = n
#print(len1 , len2)
print(min(len1,len2))
