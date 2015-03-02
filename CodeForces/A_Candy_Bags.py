'''
Created on ٠٩‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n = int(input())
nn = n ** 2
#target = (int((nn / 2) * (nn + 1)) // n)
#print(target)
#num = [int(x) for x in range(1,nn+1)] 
#lis = []
for i in range(0 , n * n//2 ):
    print(i+1 , nn - i, end = ' ')
    if (i+1) % (n//2) == 0:
        print()