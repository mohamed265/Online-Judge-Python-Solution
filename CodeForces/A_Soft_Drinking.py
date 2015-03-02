'''
Created on ١١‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = [int(x) for x in input().split()]
totalNl = int(t[1]) * int(t[2])
totalSlice = int(t[3]) * int(t[4])
p = int(t[5])
print(min (totalNl // int(t[6]) , totalSlice , p // int(t[7])) // int(t[0]))
