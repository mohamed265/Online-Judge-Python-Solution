'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
a1 = int(t[0])
a2 = int(t[1])
a3 = int(t[2])
a4 = int(t[3])
s = input()
print(a1 * s.count('1') + a2 * s.count('2') + a3 * s.count('3') + a4 * s.count('4'))
