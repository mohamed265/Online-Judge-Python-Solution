'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
t = {}#{str , int}
for i in range(n):
    temp = input()
    if t.__contains__(temp):
        t[temp]+= 1
    else:
        t[temp] = 1
print (max(t.values()))