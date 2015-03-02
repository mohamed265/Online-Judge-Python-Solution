'''
Created on ٠٧‏/١٢‏/٢٠١٤

@author: mohamed265
'''
a , b , c = int(input()) , int(input()), int(input())
t = []
t1 = a + b + c
t2 = a * b * c
t3 = (a * b) + c
t4 = (a + b) * c
t5 = a * (b + c)
t6 = a + (b * c)
print(max(t1,t2,t3,t4,t5,t6))
