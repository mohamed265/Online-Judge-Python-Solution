'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
 temp  = 0
def fun(a , b):
    slon = 0
    while a != 0 :
        slon += ((a // b) * b) 
        temp += a % b
        a //= b
    return  slon
    
t = input().split()
a = int(t[0])
b = int(t[1])
del t
slon = fun(a,b)
while temp > 0:
    a =  temp 
    temp = 0
    slon += fun(a,b)

    #a += t
print(slon)
    #input()
