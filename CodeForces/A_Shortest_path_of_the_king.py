'''
Created on ١١‏/١٢‏/٢٠١٤

@author: mohamed265
'''
s = input()
t = input()
lis = []
while s != t:
    r = ""
    if s[0] > t[0]:
        r += "L"
        s = chr(ord(s[0]) - 1) + s[1]
    elif s[0] < t[0]:
        r += "R"
        s = chr(ord(s[0]) + 1) + s[1]
        
    if s[1] > t[1]:
        r += "D"
        s = s[0] + chr(ord(s[1]) - 1)
    elif s[1] < t[1]:
        r += "U"
        s = s[0] + chr(ord(s[1]) + 1)
    lis.append(r)
print(len(lis))
for i in range(len(lis)):
    print(lis[i])
