'''
Created on ٠٢‏/٠١‏/٢٠١٥

@author: mohamed265
'''
def dfs(i):
    if i == size + 1:
        return
    temp[i] = False
    for j in range(size):
        if (X[j] == X[i] or Y[j] == Y[i]) and temp[j] :
            dfs(j) 
size = int(input())
X = []
Y = []
temp = [True for i in range(size)]

for i in range(size):
    t = input().split()
    X.append(int(t[0]))
    Y.append(int(t[1]))
    
slon = -1
for i in range(size):
    if temp[i]:
        dfs(i)
        slon+=1
print(slon)