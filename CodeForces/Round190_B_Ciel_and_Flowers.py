'''
Created on Jan 27, 2015

@author: mohamed265
'''
temp = input().split()
r = int(temp[0])
g = int(temp[1])
b = int(temp[2])
rr = r // 3
bb = b // 3
gg = g // 3
slon1 = min(r % 3, g % 3, b % 3) + rr + bb + gg
rrr = (3 if r >= 3 else 0)
slon2 = (rr - 1) + bb + gg + min(r % 3 + rrr, g % 3, b % 3)

bbb = (3 if b >= 3 else 0)
slon3 = (bb - 1) + rr + gg + min(b % 3 + bbb, g % 3, r % 3)

ggg = (3 if g >= 3 else 0)
slon4 = (gg - 1) + bb + rr + min(g % 3 + ggg, r % 3, b % 3)

print(max(slon1, slon2, slon3, slon4))
