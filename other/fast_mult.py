def binNum(x):
    mas = []
    last_bit = 0
    while x != 0:
        last_bit = x & 1
        mas.append(last_bit)
        x = x >> 1
    return mas

def fastMulty(a, x, p):
    if x < 0:
        x = p + x
    y = 1
    s = a
    masBin = binNum(abs(x))
    for i in range(len(masBin)):
        if masBin[i]==1:
            y = y *s%p
        s = s * s%p

    return y