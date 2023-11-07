from other.simple_num import generate_simpleNum 
from other.fast_mult import fastMulty
from lab2.shamir import generateC_D
from other.fast_mult import fastMulty
from other.sha256_hash import sha256_hash

def proverkaCertif():
    pass

def makeCertif():
    with open('labTxt/messege.txt', 'r') as f:
        messege = f.read()
        f.close
    hash = sha256_hash(messege)
    hash_list = list(hash)
    

def el_gamal_signature():
    makeCertif()
    proverkaCertif()