t = input().split()
n = int(t[0])
m = int(t[1])
del t
t = [int(x) for x in input().split()]
'''
slon = t.count(m)
if slon != 0:
    t.remove(m)
n = len(t)
'''
slon = 0
temp = 0
for i in range(n):
    temp = t[i]
    t[i] = 0
    for j in range(n):
        if temp + t[j] <= m:
            temp += t[j]
            t[j] = 0
        else:
            break
    if temp != 0:
        slon += 1
    #print(t)
print(slon)
'''
    if temp[i] > m:
        temp[i + 1] += (temp[i] - m)
        slon += 1
    elif temp[i] < m:
        temp[i + 1] += temp[i]
    else:
        slon += 1
slon += (temp[n - 1] // m) + (0 if temp[n - 1] % m == 0 else 1)
print(slon)
    '''
