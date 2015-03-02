'''
Created on ٢٧‏/١١‏/٢٠١٤

@author: mohamed265
'''
n = input()
list = input().split()
one = []
two = []
three = []

for i , x in enumerate(list):
    if x == '1':
        one.append(i+1)
    elif x == '2':
        two.append(i+1)
    else:
        three.append(i+1)

size = min(len(one) , len(two) , len(three))

print(size)
for j in range(size):
    print(one[j],two[j],three[j])