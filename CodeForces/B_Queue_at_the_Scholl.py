'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
temp = input().split()
b = int(temp[1])
del temp
s = input()
le = len(s)
for j in range(b):
    temp = ""
    flag = False
    for i in range(le):
        if i != le - 1:
            if flag:
                temp += "B"
                flag = False
            elif s[i] == 'B' and s[i + 1] == 'G':
                temp += "G"
                flag = True
            else:
                temp += s[i]
        elif flag:
            temp += "B"
        else:
            temp += s[i]
    s = temp

print(s)
