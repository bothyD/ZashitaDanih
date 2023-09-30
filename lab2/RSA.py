import random
from other.simple_num import generate_simpleNum 
from other.evklidGCD import EvklidGCD 
from lab1.gen_evklid import GenEvklid
from lab2.shamir import generateC_D
from other.fast_mult import fastMulty

def generateC_D(p):
    while True:
        c = random.randint(1, p-1)
        if EvklidGCD(p,c) == 1:
            break
    U = GenEvklid(p,c)
    d = U[2]
    if (c*d)%(p) != 1 or d<0:
        c, d = generateC_D(p)
    return c, d  

def RSA():
    m=282
    q = generate_simpleNum()
    p = generate_simpleNum()
    N= q*p
    fu = (p-1)*(q-1)
    d, c = generateC_D(fu)
    print("p = ",p, ", q = ", q, ", N = ", N, "\nfu = ", fu, ", d = ", d, ", c = ", c)
    # step 1
    e = fastMulty(m, d, N)
    # step 2
    m2 = fastMulty(e,c,N)
    print("m = ",m, ", m` = ", m2)