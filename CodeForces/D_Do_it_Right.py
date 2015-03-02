'''
Created on ٠٥‏/٠١‏/٢٠١٥

@author: mohamed265
'''
import math
t = input().split()
c = int(t[0]) * int(t[0]) + int(t[1]) * int(t[1]) 
k = int(math.sqrt(c))
k = k ** 2
if int(k) == int(c):
    print("YES")
    exit(0)
c = int(t[0]) * int(t[0]) - int(t[1]) * int(t[1])
if c > 0: 
    k = int(math.sqrt(c))
    k = k ** 2
    if int(k) == int(c):
        print("YES")
        exit(0)
c = int(t[1]) * int(t[1]) -  int(t[0]) * int(t[0])
if c > 0:
    k = int(math.sqrt(c))
    k = k ** 2
    if int(k) == int(c):
        print("YES")
        exit(0)
print("NO")