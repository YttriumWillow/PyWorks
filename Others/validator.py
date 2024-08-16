import random as r

g = lambda : r.sample([1,2,3,4,5,6,7,8,9], 4)

l = []

for i in range(100):
    u = r.randint(1, 100)
    v = r.randint(1, 100)
    
    if u <= u ^ v <= v:
        print (u, u ^ v, v)
        print (bin(u)[2:].zfill(7))
        print (bin(v)[2:].zfill(7))
        print (bin(u^v)[2:].zfill(7))