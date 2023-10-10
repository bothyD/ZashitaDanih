from other.fast_mult import fastMulty
from lab1.dif_helman import generate_g, generate_q_p
from other.split_massege import generate_masM_kolIter
import random

def el_gamal():
    with open('labTxt/messege.txt', 'r') as f:
        m = int(f.read())
    #генерируем открытое p и g
    q, p  = generate_q_p() 
    g = generate_g(q, p)
    print("p = ", p, ", g = ", g)
    mas_m,  kol_iter = generate_masM_kolIter(m,p)

    # Ci - закрытое, Di - открытое,
    Cb = random.randint(2, p-1)
    Db = fastMulty(g,Cb,p)
    print("Cb = ", Cb, ", Db = ", Db)
    k = random.randint(2, p-2)
    r = fastMulty(g,k,p)
    print(mas_m)
    with open('labTxt/file_encode.txt', 'w') as f:

        for i in range(kol_iter):
            #шаг со стороны А
            e =(int(mas_m[i])* fastMulty(Db,k,p))%p
            f.write(str(e)+"\n")
            print("r = ", r, ", e = ", e)
        f.close
    with open('labTxt/file_encode.txt', 'r') as f:
        lines = f.readlines()
        f.close
    print(lines)
    with open('labTxt/file_decode.txt', 'w') as f:
        for i in lines:
            #шаг со стороны В
            e = int(i)
            m2 =(e* fastMulty(r,p-1-Cb,p))%p
            f.write(str(m2))
        f.close



