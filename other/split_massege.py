def split_string(string, n):
    length = len(string)
    part_length = length // n
    parts = []
    for i in range(n-1):
        parts.append(string[i*part_length:(i+1)*part_length])
    parts.append(string[(n-1)*part_length:])
    return parts

def generate_masM_kolIter(m,p):
    mas_m = []
    if m < p:
        kol_iter = 1
        mas_m.append(m)
    else:
        kol_iter = len(str(m)) // len(str(p))+1
        mas_m = split_string(str(m), kol_iter)
    return mas_m, kol_iter