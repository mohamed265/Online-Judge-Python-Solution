'''
Created on ٢٧‏/١٢‏/٢٠١٤

@author: mohamed265
''' 
class TheKingsArmyDiv2:
    def getNumber(self, state):
        t1 = t2 = 2
        r = len(state[0])
        c = len(state)
        for i in range(c):
            for j in range(r-1):
                if state[i][j] == 'H' and state[i][j+1] == 'H':
                    return 0
                elif state[i][j] == 'H' and state[i][j+1] == 'S':
                    t1 = 1
        
        for j in range(r):
            for i in range(c-1):
                if state[i][j] == 'H' and state[i+1][j] == 'H':
                    return 0
                elif state[i][j] == 'H' and state[i+1][j] == 'S':
                    t2 = 1
            
        return min(t1,t2)
x= TheKingsArmyDiv2
print(x.getNumber(x,["SSSSS", "SSHHS","SSSSS"]))