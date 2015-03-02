'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
s = input()
l = u = 0
for c in s:
    if c == c.upper():
        u += 1
    else:
        l += 1
print(s.upper() if u > l else s.lower()) 
        
