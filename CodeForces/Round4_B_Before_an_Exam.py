t = input().split()
n = int(t[0])
sumTime = int(t[1])
tempMA = tempMI = 0
list = []
mi = []
ma = []
for i in range(n):
    t = input().split()
    tempMI += int(t[0])
    tempMA += int(t[1])
    mi.append(int(t[0]))
    ma.append(int(t[1]))
    list.append(int(t[0]))
        
if tempMI <= sumTime and sumTime <= tempMA :
    print("YES")
    if sumTime != tempMI:
        for i in range(n):
            temp = ma[i] - list[i]
            if temp + tempMI > sumTime:
                 temp = sumTime - tempMI
            list[i] += temp
            tempMI += temp
            if sumTime == tempMI:
                break
    print(' '.join(map(str , list)))
else:
    print("NO")
