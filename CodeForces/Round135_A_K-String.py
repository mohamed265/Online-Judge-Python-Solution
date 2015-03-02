'''
Created on Jan 5, 2015

@author: mohamed265
'''
k = int(input())
t = input()
ma = {}
for x in t:
    if ma.__contains__(str(x)):
        ma[x] += 1
    else:
        ma[x] = 1
flag = True
slon = ''
for x in ma:
   if ma[x] % k == 0:
        slon += (ma[x] // k) * x
   else:
       flag = False
       break
if flag:
    print(slon * k)
else:
    print(-1)
