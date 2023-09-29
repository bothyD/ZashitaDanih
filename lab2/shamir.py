import random
from other.fast_mult import fastMulty
from other.is_prime import is_prime
from other.evklidGCD import EvklidGCD
from lab1.gen_evklid import GenEvklid


def generate_p():
    p = random.randint(10**4, 10**5)
    while not is_prime(p):
        p = random.randint(10**4, 10**5)
        
    return p

def generateC(p):
    while True:
        c = random.randint(10**4, 10**5)
        if EvklidGCD(p-1,c) == 1:
            break
        
    return c
        
def generateD(p, Ca):
    U = GenEvklid(p-1,Ca)
    return U[2]


def shamir():
    p = generate_p()
    Ca = generateC(p)
    Da = generateD(p, Ca)
    print("p = ",p, ", Ca = ", Ca, ", Da = ", Da)
    if (Ca*Da)%(p-1) != 1:
        print("Error init params. Try again")
        return
    print((Ca*Da)%(p-1)) 

    