def split_string(s, n):
    result = [s[i:i+n] for i in range(0, len(s)-n, n)]
    result.append(s[(len(s)//n)*n:])
    return result

def generate_masM_kolIter(m,p):
    mas_m = []
    if m < p:
        kol_iter = 1
        mas_m.append(m)
    else:
        kol_iter = len(str(p))-1
        mas_m = split_string(str(m), kol_iter)
    kol_iter = len(mas_m)
    return mas_m, kol_iter