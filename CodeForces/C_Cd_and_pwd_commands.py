'''
Created on ١١‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
t = ['']
temp = ""
for i in range(n):
    temp = input()
    if temp == 'pwd':
        for x in t:
            print(x, end='/')
        print()
    else:
        temp = temp.split()
        temp = temp[1].split('/')
        #print(temp)
        if temp[0] == '':
            t = []
        for x in temp:
            if x == '..':
                t.pop(len(t)-1)
            else :
                t.append(x)
                    
       # print(temp)
