'''
Created on ١٣‏/١٢‏/٢٠١٤

@author: mohamed265
'''
input()
a = sorted(input().split(), key=int)
#print(a)
print(a[-1], ' '.join(a[1:-1]), a[0])
#print(*a)