
from other.fast_mult import fastMulty
from lab1.gen_evklid import GenEvklid
import hashlib
import random
import math

def is_prime(p):
    for x in range(1, 5):
        a = random.randrange(p-1) + 1
        if fastMulty(a, (p-1), p) != 1:
            return False
    return True

def get_prime(left, right):
    while True:
        p = random.randint(left, right)
        if is_prime(p):
            return p

def makeCertif():
    with open('labTxt/messege.txt', 'r', encoding='utf-8') as f:
        message = f.read()
    m = message.encode('utf-8')
    q = get_prime(1 << 255, (1 << 256) - 1)

    while True:  # Генерируем p
        b = random.randint(math.ceil((1 << 1023) / q), ((1 << 1024) - 1) // q)
        if is_prime(p := b * q + 1):
            break

    while True:  # Находим a
        g = random.randrange(2, p - 1)
        if (a := fastMulty(g, b, p)) > 1:
            break
        
    x = random.randint(1, q)
    y = fastMulty(a, x, p)


    h = hashlib.md5(m).hexdigest()
    print(f'GOST md5 hash: {h}')
    h = int(h, 16)

    k = random.randint(1, q)
    r = fastMulty(a, k, p) % q
    s = (k * h + x * r) % q
    while s == 0 or r == 0:
        k = random.randint(1, q)
        r = fastMulty(a, k, p) % q
        s = (k * h + x * r) % q

    with open('labTxt/certificate.txt', 'w') as f:
        f.write(str(p)+" "+ str(q)+" "+ str(y)+" "+ str(r)+" "+ str(a)+" "+ str(s))
        f.close

def proverkaCertif():
    with open('labTxt/messege.txt', 'r', encoding='utf-8') as f:
        message = f.read()
    m = message.encode('utf-8')
    h = hashlib.md5(m).hexdigest()
    h = int(h, 16)
    with open('labTxt/certificate.txt', 'r') as f:
        lines = f.readlines()
        p, q, y, r, a, s = lines[0].split(" ")
        p, q, y, r, a, s = int(p), int(q), int(y), int(r), int(a), int(s)


    temp = GenEvklid(h, q)[1]
    if temp < 1:
        temp += q
    u1 = (s * temp) % q
    u2 = (-r * temp) % q
    v = ((fastMulty(a, u1, p) * fastMulty(y, u2, p)) % p) % q

    if v==r:
        print("подпись совпала")
    else:
        print("подпись не совпала")


def gost_sign():
    makeCertif()
    proverkaCertif()