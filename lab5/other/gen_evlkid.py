def GenEvklid(a: int, b: int) -> list[int, int, int]:

    if a <= 0 or b <= 0:
        raise ValueError("Числа могут быть только натуральными")
    if a > b:
        a, b = b, a
    u = [a, 1, 0]
    v = [b, 0, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u, v = v, t
    return u

def inverse(n, p):
    gcd, inv, _ = GenEvklid(n, p)
    assert gcd == 1
    if inv < 0 :
        inv += p
    return inv