import random
from other.fast_mult import fastMulty
from other.is_prime import is_prime

def generate_q_p():
    go = True
    while go:
        q = random.randint(10**3, 10**4)
        while not is_prime(q):
            q = random.randint(10**6, 10**9)
        p = 2*q + 1
        if is_prime(p):
            go = False
    print("q = ",q, "; p = ",p)
    return q, p

def dif_helman():
    q,p = generate_q_p()
    g = 2
    while g != p-2:
        x = fastMulty(g, q, p)
        if x == 1:
            g+=1
        else:
            break
    print("g = ", g)
    xA= random.randint(10**2, 10**4)
    xB= random.randint(10**2, 10**4)
    yA = fastMulty(g, xA, p)
    yB = fastMulty(g, xB, p)
    print("yA = ", g, "^", xA," mod ", p," = ", yA)
    print("yB = ", g, "^", xB," mod ", p," = ", yB)
    Zab = fastMulty(yB, xA, p)
    Zba = fastMulty(yA, xB, p)
    print("Zab = ", yB, "^", xA," mod ", p," = ", Zab)
    print("Zba = ", yA, "^", xB," mod ", p," = ", Zba)
    print("Zab = Zba = ",Zba)
    return Zab