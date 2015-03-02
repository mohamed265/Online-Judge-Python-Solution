'''
Created on Feb 11, 2015

@author: mohamed265
'''
a = input()
b = input()
num4 = num7 = 0
for i in range(len(a)):
    if a[i] != b[i]:
        if a[i] == '4':
            num4 += 1
        else:
            num7 += 1
print(min(num4, num7) + abs(num4 - num7))
