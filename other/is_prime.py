import math

def is_prime(p):
    if p <= 1:
        return False
    b = int(math.sqrt(p))
    for i in range(2, b+1):
        if p % i == 0:
            return False
    return True