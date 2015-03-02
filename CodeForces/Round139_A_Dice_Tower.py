'''
Created on Jan 26, 2015

@author: mohamed265
'''
n = int(input())
temp = input()
temp2 = str(7 - int(temp))
for i in range(n):
    test = input()
    if test.count(temp) == 1 or test.count(temp2) == 1:
        print("NO")
        exit(0)
print("YES")
