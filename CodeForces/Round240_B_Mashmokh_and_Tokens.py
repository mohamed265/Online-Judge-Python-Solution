'''
Created on Jan 28, 2015

@author: mohamed265
'''
t = input().split()
n = int(t[0])
a = int(t[1])
b = int(t[2])
for x in input().split():
    
    w = ((int(x) * a) % b) 
    w //= a
    print (w, end=' ')
