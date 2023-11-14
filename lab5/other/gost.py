
from other.fast_mult import fastMulty
from other.gen_evlkid import GenEvklid
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

def makeCertif(message):
    m = message.encode('utf-8')
    h = hashlib.md5(m).hexdigest()
    h = int(h, 16)
    
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

    k = random.randint(1, q)
    r = fastMulty(a, k, p) % q
    s = (k * h + x * r) % q
    while s == 0 or r == 0:
        k = random.randint(1, q)
        r = fastMulty(a, k, p) % q
        s = (k * h + x * r) % q
    publicData = {'p':p,'q': q,'a': a, 'y':y, 'm':m, 'r':r, 's':s}
    return publicData


def proverkaCertif(dict):
    p = dict['p']
    q = dict['q']
    y = dict['y']
    m = dict['m']
    r = dict['r']
    s = dict['s']
    a = dict['a']

    h = hashlib.md5(m).hexdigest()
    h = int(h, 16)

    temp = GenEvklid(h, q)[1]
    if temp < 1:
        temp += q
    u1 = (s * temp) % q
    u2 = (-r * temp) % q
    v = ((fastMulty(a, u1, p) * fastMulty(y, u2, p)) % p) % q

    if v==r:
        print("подпись корректна")
    else:
        print("подпись не корректна")
