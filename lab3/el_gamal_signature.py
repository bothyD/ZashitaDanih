from other.simple_num import generate_simpleNum 
from other.fast_mult import fastMulty
from other.fast_mult import fastMulty
from other.sha256_hash import sha256_hash
from other.is_prime import is_prime
from other.evklidGCD import EvklidGCD
import random

def find_primitive_root(P):
    for g in range(2, P):
        # Проверяем, является ли g первообразным корнем
        is_primitive_root = True
        residues = set()
        for x in range(1, P - 1):
            residue = fastMulty(g, x, P)
            if residue in residues:
                is_primitive_root = False
                break
            residues.add(residue)
        if is_primitive_root:
            return g
    return None

def proverkaCertif():
    with open('labTxt/messege.txt', 'r') as f:
        messege = f.read()
        f.close
    hash = sha256_hash(messege)
    hash_list = list(hash)

    with open('labTxt/certificate.txt', 'r') as f:
        lines = f.readlines()
        
        r, y, p, g = lines[0].split(" ")
        r, y, p, g = int(r), int(y), int(p), int(g)
        certif = lines[1].split(" ")
    certif.pop()

    res_left = []
    res_right = []
    for i in range(len(certif)):
        left= ((y**r)*(r**int(certif[i])))%p
        res_left.append(left)
        right = fastMulty(g,hash_list[i],p)
        res_right.append(right)                                                                                                                                                                                                                                                                                                                                                                                                                    
    if res_left == res_right:
        print("подпись совпала")
    else:
        print("подпись не совпала")

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def makeCertif():
    with open('labTxt/messege.txt', 'r') as f:
        messege = f.read()
        f.close
    hash = sha256_hash(messege)
    hash_list = list(hash)

    p = generate_simpleNum()
    q = int((p-1)/2)
    while (p != 2*q +1) or  not is_prime(q):
        p = generate_simpleNum()
        q = int((p-1)/2)
    g = find_primitive_root(p)
    print(p, q, g)
    x = random.randint(2, p-2)
    y = fastMulty(g,x,p)
    ############## 222222222222 ###################
    k = random.randint(2, p-2)
    while EvklidGCD(k, p-1)!=1:
        k = random.randint(1, p-1)
    k_inverse = mod_inverse(k, p - 1)
    if k_inverse is None:
        raise ValueError("k^(-1) does not exist")
    r = fastMulty(g,k,p)
    ############## 333333333333 ###################
    ws = []
    for i in hash_list:
        u = ((i-x*r) % (p-1))
        s = k_inverse*u % (p-1)
        ws.append(s)
    with open('labTxt/certificate.txt', 'w') as f:
        f.write(str(r)+" "+ str(y)+" "+ str(p)+" "+str(g)+ "\n")

        for i in ws:
            f.write(str(i)+" ")
        f.close

    

def el_gamal_signature():
    makeCertif()
    proverkaCertif()