'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
 
n = int(input())
res = 0
t = {}
for i in range(n):
    t =  [int(x) for x in input().split()]#map(int, input().split())
    if t[0] + t[1] + t[2] > 1 : res+=1
print(res)
'''
n = int(input())
res = 0
for i in range(n):
    t = [int(x) for x in input().split()]
    res = res + 1 if t[0] + t[1] + t[2] > 1 else res
print(res)
'''