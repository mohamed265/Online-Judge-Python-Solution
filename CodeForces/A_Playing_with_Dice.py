'''
Created on ١١‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = [int(x) for x in input().split()]
fWin = sWin = draw = 0
for i in range(1,7):
    if abs(t[0] - i) < abs(t[1] - i):
        fWin += 1
    elif abs(t[0] - i) > abs(t[1] - i):
        sWin +=1
    else:
        draw +=1
print(fWin ,draw, sWin)