import random
from other.simple_num import generate_simpleNum 
from other.evklidGCD import EvklidGCD 
from lab1.gen_evklid import GenEvklid
from lab2.shamir import generateC_D
from other.fast_mult import fastMulty
from other.split_massege import generate_masM_kolIter

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
    with open('labTxt/messege.txt', 'r') as f:
        m = int(f.read())
    q = generate_simpleNum()
    p = generate_simpleNum()
    N= q*p
    fu = (p-1)*(q-1)
    d, c = generateC_D(fu)

    mas_m,  kol_iter = generate_masM_kolIter(m,p)

    print("p = ",p, ", q = ", q, ", N = ", N, "\nfu = ", fu, ", d = ", d, ", c = ", c)
    with open('labTxt/file_encode.txt', 'w') as f:
        for i in range(kol_iter):
            # step 1
            e = fastMulty(int(mas_m[i]), d, N)
            f.write(str(e)+"\n")
            print("e = ", e)
        f.close
    with open('labTxt/file_encode.txt', 'r') as f:
        lines = f.readlines()
        f.close
    with open('labTxt/file_decode.txt', 'w') as f:
        for i in lines:
            # step 2
            e = int(i)
            m2 = fastMulty(e,c,N)
            f.write(str(m2))
        f.close
