'''
Created on Jan 6, 2015

@author: mohamed265
'''
t = input().split()
x = int(t[0])
y = int(t[1])
if x > 0 and y > 0:
    print(0, x + y, x + y, 0)
elif x < 0 and y > 0:
    print(x + -1 * y, 0, 0, -1 * x + y)
elif x < 0 and y < 0:
    print(x + y, 0, 0, x + y)
else:
    print(0, -1 * x + y, x + -1 * y , 0)
    
