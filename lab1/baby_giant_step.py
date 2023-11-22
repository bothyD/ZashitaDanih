from other.fast_mult import fastMulty
from other.is_prime import is_prime
from lab1.gen_evklid import GenEvklid 
import random
import math

def generate_m_k(p):
    m  = int(math.sqrt(p)) 
    k= m
    while k*m<p:
        m+=1
    return m, k

def bgs():
    print(fastMulty(11,5,23))
    print(fastMulty(20,5,23))
    print(fastMulty(21,5,23))
    
    # temp = GenEvklid(6, 11)[1]
    # if temp < 1:
    #     temp += 11
    # print(temp)
    # y =  9
    # a = 2
    # p = random.randint(10**1, 10**2)
    # while not is_prime(p):
    #     p = random.randint(10**1, 10**2)
    # m, k = generate_m_k(p)
    # print("p = ", p, "; m = ", m, "; k = ", k)
    # baby = {fastMulty(a, j, p) * y % p: j for j in range(m)}
    # giant = [fastMulty(a, (m * i), p) for i in range(1, k + 1)]
    # print("baby - ", baby)
    # print("giant - ", giant)
    # for i, el in enumerate(giant, 1):
    #     if (j := baby.get(el)) is not None:
    #         x = i * m - j
    #         break
    #     else:
    #         x = "Not found"
    # print("a^(i*m) = a^j * y\n")
    # print(a, "^(", i, "*", m, ") = ",  (pow(a,(i*m)))%p) 
    # print(a, "^", j, " * ", y," = ", ((pow(a,j))*y)%p)

    # print("\nx = i*m-j = ", i,"*",m, "-", j, " = ", i*m-j)
    # print(x)
    # return(x)