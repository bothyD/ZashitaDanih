from other.simple_num import generate_simpleNum 
from other.fast_mult import fastMulty
from lab2.shamir import generateC_D
from other.fast_mult import fastMulty
from other.sha256_hash import sha256_hash
from other.is_prime import is_prime

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
    pass

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

def el_gamal_signature():
    makeCertif()
    proverkaCertif()