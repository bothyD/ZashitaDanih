from other.simple_num import generate_simpleNum 
from other.evklidGCD import EvklidGCD
from other.fast_mult import fastMulty
from other.split_massege import generate_masM_kolIter
from lab2.shamir import generateC_D
from other.fast_mult import fastMulty

import hashlib

def RSA_signature():
    with open('labTxt/messege.txt', 'r') as f:
        messege = f.read()
    q = generate_simpleNum()
    p = generate_simpleNum()
    N= q*p
    fu = (p-1)*(q-1)
    d, c = generateC_D(fu+1)
    y = hashlib.sha256(messege.encode()).hexdigest()
    hashed_int = int(y, 16)
    print(hashed_int)
    s = fastMulty(y,c,N)
    print(s)