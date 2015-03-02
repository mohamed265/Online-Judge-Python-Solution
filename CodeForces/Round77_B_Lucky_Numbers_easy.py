'''
Created on Jan 28, 2015

@author: mohamed265
'''
num = input()
def fun(temp , size4 , size7):
    if size4 == 0 and size7 == 0:
        if int(temp) >= int(num):
            return int(temp)
        else:
            return 999999999999999999999999
    if size4 == 0:
        for i in range(size7):
            temp += "7"
        if int(temp) >= int(num):
            return int(temp)
        else:
            return 999999999999999999999999
    if size7 == 0:
        for i in range(size4):
            temp += "4"
        if int(temp) >= int(num):
            return int(temp)
        else:
            return 999999999999999999999999
    
    t1 = fun(temp + "4", size4 - 1, size7) 
    t2 = fun(temp + "7", size4, size7 - 1)
    return t1 if t1 < t2 else t2
 
le = len(num) + (0 if len(num) % 2 == 0 else 1)
for i  in range (le, 14, 2):
    re = fun("", i // 2, i // 2)
    if re != 999999999999999999999999:
        print(re)
        exit(0)
