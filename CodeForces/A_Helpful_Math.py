'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
s = [int(x) for x in input().split('+')]
s.sort()
t = ""
i = 0
for x in s :
    if i == len(s) -1:
        break
    print(x,end='+')
    i+=1
print(s[len(s)-1])