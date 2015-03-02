'''
Created on ٠٦‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
t = int(t[1])
t -= 1
if n % 2 == 0 and t >= n // 2 :
    t += 1
# if n % 2 == 0:
if t < n / 2:
    print(2 * t + 1)
else:
    print (2 * (t - n // 2))
# else:
    
