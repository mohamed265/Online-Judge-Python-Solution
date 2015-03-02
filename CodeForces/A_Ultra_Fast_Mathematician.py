'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
s , b = input() , input()

for i in range(len(s)):
    if s[i] == b[i]:
        print('0' , end='')
    else:
        print('1', end='')
