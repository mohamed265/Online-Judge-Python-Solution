'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
# 
 
def toExcel (x):
    
    num1 = num2 = 0 
    try:
        s = x.split(sep='R')
        t = s[1].split(sep='C')
        num2 = int(t[0])
        num1 = int(t[1])
        # print(num1,num2)
        # num1-=1
    except Exception:
        return 0
    tt = ""
    while num1 > 0:
        if num1 % 26 == 0:
            tt = 'Z' + tt
            num1 -= 1
            # num1 //= 26
        else:  # '''
            tt = chr(num1 % 26 + 64) + tt
        num1 //= 26
        
    return tt + str(num2) 
    
def ToOther (x):
    num = 0
    ch2 = ch = ""
    try:
        for i in x:
            # print(i)
            if i >= 'A' and i <= 'Z':
                ch += i
            else:
                ch2 += i
        num = int(ch2)
    except Exception:
        return 0
    slon = "R" + str(num) + "C"
    num = 0
    for i in range(len(ch)):
        num += (ord(ch[i]) - 64) * (26 ** ((len(ch) - 1) - i))
    return slon + str(num)  # + ord(ch[len(ch) - 1]) - 64)
# print(toExcel("R1C79"))
#print(ToOther("ABD815"))

n = int(input())
for i in range(n):
    t = input()
    c = toExcel(t)
    if (isinstance(c,str)):
        print(c)
    else:
        print(ToOther(t))
#'''
# #t1 = t4 = t3 = t2 = ""
# #for i in range(len(t)):
# #  if t
