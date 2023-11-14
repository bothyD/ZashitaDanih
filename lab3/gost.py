from other.is_prime import is_prime
from other.fast_mult import fastMulty
import secrets
import random
import math
# from sympy import isprime
from other.sha256_hash import sha256_hash
import hashlib

def get_prime(start, end):
    for num in range(start, end + 1):
        if isprime(num):
            return num


def gost():
    with open('labTxt/messege.txt', 'r', encoding='utf-8') as f:
        message = f.read()

    # Кодируем строку в байты перед хешированием
    encoded_message = message.encode('utf-8')
    # Вычисление MD5 хеша
    h = hashlib.md5(encoded_message).hexdigest()
    print(f'GOST md5 hash: {h}')

    # Преобразование хеша в целое число
    h = int(h, 16)
    print(h)
    q = get_prime(1 << 11, (1 << 12) - 1)

    while True:  # Генерируем p
        b = random.randint(math.ceil((1 << 21) / q), ((1 << 22) - 1) // q)
        if is_prime(p := b * q + 1):
            break

    while True:  # Находим a
        g = random.randrange(2, p - 1)
        if (a := fastMulty(g, b, p)) > 1:
            break
    print(q," ", p, " ", a)
    x = random.randint(1, q)
    y = fastMulty(a, x, p)

    
    k = random.randint(1, q)
    r = fastMulty(a, k, p) % q
    s = (k * h + x * r) % q
    while s == 0 or r ==0:
        k = random.randint(1, q)
        r = fastMulty(a, k, p) % q
        s = (k * h + x * r) % q
    print(s," ", r, " ", k)

    u1 = (s * (h^-1)) % q
    u2 = (-r * (h^-1)) % q
    v = ((fastMulty(a, u1, p) * fastMulty(y, u2, p)) % p) % q


    if v == r:
        print(True)
    else:
        print(False)
    
