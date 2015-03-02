'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
n  = input().split()
rse = int(n[0]) // int(n[2]) if int(n[0]) % int(n[2]) == 0 else int(n[0]) // int(n[2]) + 1
rse *= int(n[1]) // int(n[2]) if int(n[1]) % int(n[2]) == 0 else int(n[1]) // int(n[2]) + 1
print(rse)