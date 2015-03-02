'''
Created on Jan 31, 2015

@author: mohamed265
'''
def summ(x):
    temp = 0
    while x != 0:
        temp += x % 10
        x //= 10
    return temp

def constract(x):
    temp = ""
    while x > 9: 
        if x > 9:
            temp = '9' + temp
            x -= 9
    if x != 0:
        return chr(x+48) + temp;
    return temp
mi = [0 for x in range(301)]
firstTime = [0 for x in range(301)]
patern = [0 for x in range(301)]
for i in range(1, 301):
    mi[i] = int(constract(i))
    #print(mi[i])
    temp = summ(i)
    if firstTime[temp] == 0:
        firstTime[temp] = i
    elif patern[temp] == 0:
        patern[temp] = i - firstTime[temp] 
n = int(input())
j = 1
last = 0
for i in range(n):
    temp = int(input())
    if mi[temp] > last:
        last = mi[temp]
    else:
        last = mi[temp] +1
        while summ(last) != temp:
            last += 1;
    print(last)
        
'''

  '''  