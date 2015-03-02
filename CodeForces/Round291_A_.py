'''
Created on Feb 14, 2015

@author: mohamed265
'''
x = input()
slon = ""
for i in range(1, len(x)):
    inverted = ord('9') - ord(x[i])
    if x[i] < '5':
        slon += chr(int(x[i]) + 48)
    else:
        slon += chr(inverted + 48)
inverted = ord('9') - ord(x[0])
if inverted == 0 or int(x[0]) <= int('4') :
    print(x[0], end='')
else:
     print(inverted, end='')
print(slon)
