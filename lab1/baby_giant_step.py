from other.fast_mult import fastMulty
from other.is_prime import is_prime
import random
import math

def generate_m_k(p):
    m  = int(math.sqrt(p)) 
    k= m
    while k*m<p:
        m+=1
    return m, k

def bgs():
    y =  9
    a = 2
    p = random.randint(10**1, 10**2)
    while not is_prime(p):
        p = random.randint(10**1, 10**2)
    m, k = generate_m_k(p)
    print("p = ", p, "; m = ", m, "; k = ", k)
    baby = {fastMulty(a, j, p) * y % p: j for j in range(m)}
    giant = [fastMulty(a, (m * i), p) for i in range(1, k + 1)]
    print("baby - ", baby)
    print("giant - ", giant)
    for i, el in enumerate(giant, 1):
        if (j := baby.get(el)) is not None:
            x = i * m - j
            break
        else:
            x = "Not found"
    print("a^(i*m) = a^j * y\n")
    print(a, "^(", i, "*", m, ") = ",  (a**(i*m))%p) 
    print(a, "^", j, " * ", y," = ", ((a**j)*y)%p)

    print("\nx = i*m-j = ", i,"*",m, "-", j, " = ", i*m-j)
    print(x)
    return(x)