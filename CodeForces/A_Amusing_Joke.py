'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''
f = input() + input()
s = input()
#print (f,s)
t =[chr(x) for x in range(65 , 91)]
#print(t)
flag = True
for x in t:
    if s.count(str(x)) != f.count(str(x)):
        flag = False
        print("NO")
        break
if flag:
    print("YES")