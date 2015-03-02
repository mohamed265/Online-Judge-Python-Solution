'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''
c = int(input())
for i in range(c):
    t = int(input())
    n = 360 / (180 -t)
#print(n)
    print ("YES") if n == int(n) else print("NO")