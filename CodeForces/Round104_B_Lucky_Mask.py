'''
Created on Feb 11, 2015

@author: mohamed265
'''
def mask (a):
    temp = ''
    lenA = len(a)
    for i in range(lenA): 
        if a[i] == '4' or a[i] == '7':
            temp += a[i]
    return temp
temp = input().split()
a = int(temp[0]) + 1 
b = temp[1]
while mask(str(a)) != b:
    a += 1
print(a)
'''
temp = input().split()
a = temp[0]
b = temp[1]
t = ""
lenA = len(a)
lenBefore = len(b)
o = 0
for i in range(lenA):
    if a[i] == '4' or a[i] == '7':
        if b[o] == a[i]:
            o += 1
        else:
            break
for i in range(o , len(b)):
    t += b[i]
b = t
#print(t)
lenB = len(b)
if lenB == 0:
    if lenBefore == lenA:
        print(1,a,sep= '')
        exit(0)
    else:
        flag = True
        for i in range(lenA - lenBefore , -1 , -1):
            if int(solu[i]) < 9:
                flag = False
                solu[i] = int(solu[i]) + 1
                break
            else:
                solu[i] = 0
        if flag:
            print(1, end='')
        print(*solu, sep='')
            
if lenA < lenB:
    print(b)
elif lenA == lenB:
    if a[0] < b[0]:
        print(b)
    else:
        for i in range(1, lenA):
            if lenA[i] < lenB[i]:
                print(b)
                exit(0)
            elif a[i] > b[i]:
                break
        # print(1, b, sep='') 
else:
    solu = [0] * lenA
    j = 0
    for i in range(lenA - lenB, lenA):
        solu[i] = b[j]
        j += 1
    for i in range(lenA - lenB):
        solu[i] = a[i]
    flag = False if a[lenA - lenB] < b[0] else True
    if flag:
        j = lenA - lenB - 1
        for i in range(j , -1 , -1):
            if int(solu[i]) < 9:
                flag = False
                solu[i] = int(solu[i]) + 1
                break
            else:
                solu[i] = 0
        if flag:
            print(1, end='')
    print(*solu, sep='')

    for i in range(lenB):
        solu[i] = ord(b[i]) - ord('0')
    if flag:
        slo[lenB] += 1
    '''
    
    
