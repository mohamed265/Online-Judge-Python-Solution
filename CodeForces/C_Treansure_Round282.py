'''
Created on ١٣‏/١٢‏/٢٠١٤

@author: mohamed265
'''
s = input().split(')(')
n = len(s)
tempO = tempC = temp = 0
#print(s)
for i in range(n):
    if s[i] != '':
        temp = s[i].count('#')
        if temp == 1:
            tempO = s[i].count('(') + 1 
            tempC = s[i].count(')') + 1
            if i == n-1:
                tempC -= 1
            if i == 0:
                tempO -= 1
            print(-1) if tempC >= tempO else print(tempO-tempC)
        else:
            s[i] = '(' + s[i] + ')'
            if i == 0:
                s[i] = s[i][1:]
            if i == n-1:
                s[i] = s[i][0:-1]
            s[i] += '.'
            #print(s[i])
            tempb = numOfHash = 0
            for x in s[i]:
                if x == '(' and numOfHash == 0:
                    tempb += 1
                elif x == ')':
                    tempb -= 1
                elif x == '#':
                    numOfHash += 1
                else:
                    for i in range(numOfHash - 1):
                        if tempb != 0:
                            print(1)
                            tempb -= 1
                        else:
                            print(-1)
                    if numOfHash != 0 :
                        print(tempb) if tempb != 0 else print(-1)
                    numOfHash = 0
                    tempb = 1
                    
                
                
            #t = s[i].split('#')
            #print(t)
        #((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#((#())((((#

        '''
            continue
        temp += 1
        print(temp - s[i].count(')'))
        temp = 0
        (((##)(#(#)
        '''