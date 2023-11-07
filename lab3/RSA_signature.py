from other.simple_num import generate_simpleNum 
from other.fast_mult import fastMulty
from lab2.shamir import generateC_D
from other.fast_mult import fastMulty
from other.sha256_hash import sha256_hash

def proverkaCertif():
    with open('labTxt/messege.txt', 'r') as f:
        messege = f.read()
        f.close
    hash = sha256_hash(messege)
    hash_list = list(hash)

    wS = []
    with open('labTxt/certificate.txt', 'r') as f:
        lines = f.readlines()
        
        d, N = lines[0].split(" ")
        d, N = int(d), int(N)
        certif = lines[1].split(" ")

    certif.pop()
    for i in certif:
        w = fastMulty(int(i),d,N)
        wS.append(w)
    print(hash_list)
    print("Проверка подписи: ", wS)
    if hash_list == wS:
        print("подпись совпала")
    else:
        print("подпись не совпала")

def makeCertif():
    with open('labTxt/messege.txt', 'r') as f:
        messege = f.read()
    hash = sha256_hash(messege)
    hash_list = list(hash)
    print(hash_list)

    q = generate_simpleNum()
    p = generate_simpleNum()
    N= q*p
    fu = (p-1)*(q-1)
    d, c = generateC_D(fu+1)
    
    certif = []
    # Преобразование хеша SHA-256 в целочисленный список

    for i in hash_list:
        s = fastMulty(i,c,N)
        certif.append(s)
    print("Полученная подпись: ", certif)
    with open('labTxt/certificate.txt', 'w') as f:
        f.write(str(d)+" "+ str(N)+ "\n")
        for i in certif:
            f.write(str(i)+" ")
        f.close
    print()

def RSA_signature():
    makeCertif()
    proverkaCertif()