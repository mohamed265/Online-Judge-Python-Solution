'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
n += 1
while True:
    t = set()
    tt = n
    while tt != 0:
        t.add(tt%10)
        tt//=10
    #print(len(t) , t)
    if len(t) == 4:
        print(n)
        break
    n += 1