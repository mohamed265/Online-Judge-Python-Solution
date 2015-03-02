'''
Created on ٠٧‏/١٢‏/٢٠١٤

@author: mohamed265

m = "mohamed"
print('*'.join(m))
'''
n = int(input())
lis = []
for i in range(n):
    t = ""
    t += '  ' * abs(n - i)
    for j in range(i + 1):
        t += (str(j) + " ")
    for j in range(i - 1 , 0, -1):
        t += (str(j) + " ")
    t += '0'
    if i == 0:
        t = '  ' * abs(n - i) + '0'
    print(t)
    lis.append(t)
for i in range(n + 1):
    print(i , end=' ')
for i in range(n - 1, 0, -1):
    print(i , end=' ')
print(0,end='\n')
for i in range(len(lis)):
    print(lis[len(lis) - i - 1])
