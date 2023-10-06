import random
from other.fast_mult import fastMulty
from other.evklidGCD import EvklidGCD
from other.simple_num import generate_simpleNum
from lab1.gen_evklid import GenEvklid
from other.split_massege import generate_masM_kolIter

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
    m = 2281201
    p = generate_simpleNum()
    Ca, Da = generateC_D(p)
    Cb, Db = generateC_D(p)    
    print("\tp = ",p, "\nCa = ", Ca, ", Da = ", Da, "\nCb = ", Cb, ", Db = ", Db)
    mas_m,  kol_iter = generate_masM_kolIter(m,p)

    with open('labTxt/file_encode.txt', 'w') as f:
        for i in range(kol_iter):
            #step 1
            x1 = fastMulty(int(mas_m[i]), Ca, p)
            #step 2
            x2 = fastMulty(x1, Cb, p)
            #step 3
            x3 = fastMulty(x2, Da, p)
            f.write(str(x3)+"\n")
        f.close
    with open('labTxt/file_encode.txt', 'r') as f:
        lines = f.readlines()
        f.close
    with open('labTxt/file_decode.txt', 'w') as f:
        for i in lines:
            #step 4
            x3 = int(i)
            x4 = fastMulty(x3, Db, p)
            f.write(str(x4))
        f.close


    


    