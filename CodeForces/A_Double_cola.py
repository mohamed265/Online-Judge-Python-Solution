'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
#for n in range(1, 1803):
n = int(input()) + 5
x = 5
while x < n  :
    x = (x * 2)
    if x >= n:
        break 
    #print(x)
temp = 0
if x > 5 :
    x //= 2
    temp = x // 5
else:
    x = 0
    temp = 1
    # x+=5
    
temp2 = n - x
    #print(n , "             " , temp , temp2 , x)
if temp + x >= n:
    print("Sheldon")
elif 2 * temp + x >= n:
    print("Leonard")
elif 3 * temp + x >= n:
    print("Penny")
elif 4 * temp + x >= n:
    print("Rajesh")
else:
    print("Howard")
