import random

def EvklidGCD(a,b):
    while b !=0:
        r = a%b 
        a = b
        b = r
    return a

def GenEvklid(a, b):
    u = [a, 1, 0]
    v = [b, 0, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u, v = v, t
    return u

def generateC_D(p):
    while True:
        c = random.randint(10**4, 10**5)
        if EvklidGCD(p,c) == 1:
            break
    U = GenEvklid(p,c)
    d = U[2]
    if (c*d)%(p) != 1 or d<0:
        c, d = generateC_D(p)
    return c, d 