'''
Created on ٠٥‏/٠١‏/٢٠١٥

@author: mohamed265
'''
limit = 4000000
def fibonacci(num , num1):
    print(num , num1)
    if (num1 > limit):
        return 0
    temp = num if num % 2 == 0 else 0
    temp += num1 if num1 % 2 == 0 else 0
    return temp + fibonacci(num + num1, num + num1 + num1)
    
print(fibonacci(1, 2))
