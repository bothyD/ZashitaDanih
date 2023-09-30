from other.simple_num import generate_simpleNum
from other.fast_mult import fastMulty
from lab1.dif_helman import generate_g, generate_q_p, dif_helman
import random



def el_gamal():
    m = 228
    #генерируем открытое p и g
    q, p  = generate_q_p() 
    g = generate_g(q, p)
    print("p = ", p, ", g = ", g)

    # Ci - закрытое, Di - открытое,
    Cb = random.randint(2, p-1)
    Db = fastMulty(g,Cb,p)
    print("Cb = ", Cb, ", Db = ", Db)

    #шаг со стороны А
    k = random.randint(2, p-2)
    r = fastMulty(g,k,p)
    e =(m* fastMulty(Db,k,p))%p
    print("r = ", r, ", e = ", e)

    #шаг со стороны В
    m2 =(e* fastMulty(r,p-1-Cb,p))%p

    print("m` = ", m2)


