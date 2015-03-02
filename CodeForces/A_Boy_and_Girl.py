'''
Created on ٠٥‏/١٢‏/٢٠١٤

@author: mohamed265
'''
s = input()
t = set()
for x in s:
    t.add(x)
if len(t) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")