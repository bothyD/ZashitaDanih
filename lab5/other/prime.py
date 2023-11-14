import random
from other.fast_mult import fastMulty

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