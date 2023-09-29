def GenEvklid(a, b):
    if b > a:
        a, b = b, a
    U = [a,1,0]
    V = [b,0,1]
    while int(V[0]) != 0:
        q = int(U[0]) // int(V[0])
        T = [ U[0] % V[0], U[1] - q*V[1], U[2] - q*V[2] ] 
        U = V
        V = T
        print("U = ",U,"\n","V = ", V,"\n")
    
    return U 