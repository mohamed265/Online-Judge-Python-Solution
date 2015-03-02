'''
Created on ٠٨‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = input()
c = t = "" 
if n[0] != '-':
    print(n)
else:
    for i in range(len(n) - 1, -1, -1):
        if i != len(n) - 1:
            t = n[i] + t
        if i != len(n) - 2:
            c = n[i] + c
    print(max(int(t), int(c)))
            
