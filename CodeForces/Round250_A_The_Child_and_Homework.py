'''
Created on ٠١‏/٠١‏/٢٠١٥

@author: mohamed265
''' 
num = []
num.append(len(input())-2)
num.append(len(input())-2)
num.append(len(input())-2)
num.append(len(input())-2)
temp = min(num)
index = num.index(temp)
count = 0
for i in range(4):
    if i != index and num[i] >= 2 * temp:
        count += 1
temp = max(num)
index1 = num.index(temp)
count1 = 0
for i in range(4):
    if i != index1 and num[i] * 2 <= temp:
        count1 += 1
if count == 3 and count1 != 3:
    print( 'A' if index == 0 else ('B' if index == 1 else ('C' if  index == 2 else 'D')))
elif count1 == 3 and count != 3:
    print( 'A' if index1 == 0 else ('B' if index1 == 1 else ('C' if  index1 == 2 else 'D')))
else:
    print('C')