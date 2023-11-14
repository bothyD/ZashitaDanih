import random

from other.is_prime import is_prime

def generate_simpleNum():
    p = random.randint(10**4, 10**5)
    while not is_prime(p):
        p = random.randint(10**4, 10**5)
        
    return p