import random
from other.fast_mult import fastMulty
from other.evklidGCD import EvklidGCD
from other.simple_num import generate_simpleNum
from lab1.gen_evklid import GenEvklid


def generateC_D(p):
    while True:
        c = random.randint(10**4, 10**5)
        if EvklidGCD(p-1,c) == 1:
            break
    U = GenEvklid(p-1,c)
    d = U[2]
    if (c*d)%(p-1) != 1 or d<0:
        c, d = generateC_D(p)
    return c, d  


def shamir():
    m = 228
    p = generate_simpleNum()
    Ca, Da = generateC_D(p)
    Cb, Db = generateC_D(p)
    print("\tp = ",p, "\nCa = ", Ca, ", Da = ", Da, "\nCb = ", Cb, ", Db = ", Db)

    #step 1
    x1 = fastMulty(m, Ca, p)
    print("\nx1 = ", x1)
    #step 2
    x2 = fastMulty(x1, Cb, p)
    print("x2 = ", x2)
    #step 3
    x3 = fastMulty(x2, Da, p)
    print("x3 = ", x3)
    #step 4
    x4 = fastMulty(x3, Db, p)
    print("x4 = ", x4)


    


    