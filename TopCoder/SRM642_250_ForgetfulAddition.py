'''
Created on ٢٠‏/١٢‏/٢٠١٤

@author: mohamed265
'''
class ForgetfulAddition:
    def minNumber(self, expression):
        temp = 999999999999999999
        for i in range(len(expression) -1):
            #print(int(expression[0:i+1]) + int(expression[i+1:]))
            temp = min(temp , int(expression[0:i+1]) + int(expression[i+1:]))
        return temp
 
#x = ForgetfulAddition
#print(x.minNumber(x,"12"))