'''
Created on ٢٠‏/١٢‏/٢٠١٤

@author: mohamed265
'''
class BuyingTshirts:
    def meet(self, T, Q, P):
        temp = 0
        Qset = set()
        pset = set()
        for i in range(len(Q)):
            temp += Q[i]
            if temp >= T:
                Qset.add(i)
                temp -= T
        temp = 0
        for  i in range(len(P)):
            temp += P[i]
            if temp >= T:
                pset.add(i)
                temp -= T
        #print(len(Qset-pset))
        return (len(Qset&pset))
            