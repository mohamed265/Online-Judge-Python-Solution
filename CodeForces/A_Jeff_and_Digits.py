'''
Created on ١٠‏/١٢‏/٢٠١٤

@author: mohamed265
'''
finalSlon = -1
def dp(zCo , fCo, num , rem):
    global finalSlon
    if rem == 0 and len(num) != 0:
        finalSlon = max(finalSlon , int(num))
        
    if zCo == 0 and fCo == 0:
        return
    if zCo > 0 and len(num) != 0:
        dp(zCo - 1 , fCo, num + "0" , (rem * 10 + 0) % 90)
    if fCo > 0:
        dp(zCo , fCo - 1, num + "5" , (rem * 10 + 5) % 90)

n , t = input() , input()
zCount = t.count('0') 
fCount = t.count('5')
dp(zCount, fCount , "", 0)
if zCount > 0:
    print (max(finalSlon, 0))
else:
    print(finalSlon)
# print(zCount , fCount)
