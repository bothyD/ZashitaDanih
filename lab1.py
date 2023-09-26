import random
import math
import numpy 
### y = a^x mod p.

def fastMulty(a, x, p):
    y = 1
    s = a
    masBin = binNum(x)
    for i in range(len(masBin)):
        if masBin[i]==1:
            y = y *s%p
        s = s * s%p
    return y

def EvklidGCD(a,b):
    while b !=0:
        r = a%b 
        a = b
        b = r
    return a

def GenEvklid(a,b):
    U = [a,1,0]
    V = [b,0,1]
    while int(V[0]) != 0:
        q = int(U[0]) // int(V[0])
        T = [ U[0] % V[0], U[1] - q*V[1], U[2] - q*V[2] ] 
        U = V
        V = T
        print("U = ",U,"\n","V = ", V,"\n")
    
    return U 


def binNum(x):
    mas = []
    last_bit = 0
    while x != 0:
        last_bit = x & 1
        mas.append(last_bit)
        x = x >> 1
    return mas

def is_prime(p):
    if p <= 1:
        return False
    b = int(math.sqrt(p))
    for i in range(2, b+1):
        if p % i == 0:
            return False
    return True

def generate_q_p():
    go = True
    while go:
        q = random.randint(10**3, 10**4)
        while not is_prime(q):
            q = random.randint(10**6, 10**9)
        p = 2*q + 1
        if is_prime(p):
            go = False
    print("q = ",q, "; p = ",p)
    return q, p

def generate_m_k(p):
    m  = int(math.sqrt(p)) 
    k= m
    while k*m<p:
        m+=1
    return m, k


def find_duplicate_elements(array1, array2,a, p,y,m):
    for element1 in array1:
        for element2 in array2:
            if element1 == element2:
                i = array1.index(element1)
                j = array2.index(element2)
                x1 = (a**(i))%p
                x2 = ((a**j)*y)%p
                # if x1 == x2:
                return i, j  # Возвращаем первый найденный одинаковый элемент
    return None 

def main():
    ######################################################
    #                     1 часть                        #   
    ######################################################
    # print("Input a, x, p:\na:", end="")
    # a = int(input())
    # print("x: ", end="")
    # x = int(input())
    # print("p: ", end="")
    # p = int(input())
    # res = fastMulty(a, x, p)
    # print(res)
    ######################################################
    #                     2 часть                        #
    # ######################################################    
    # print("Input a, b:\na:", end="")
    # a = int(input())
    # print("b: ", end="")
    # b = int(input())
    # if b > a:
    #     a,b = b,a
    # res = GenEvklid(a,b)
    # print("U = (gcd(", a, ',', b,"), x, y) = (", res[0], ",", res[1],',', res[2], ")")
    ######################################################
    #                     3 часть                        #
    ###################################################### 
    # q,p = generate_q_p()
    # g = 2
    # while g != p-2:
    #     x = fastMulty(g, q, p)
    #     if x == 1:
    #         g+=1
    #     else:
    #         break
    # print("g = ", g)
    # xA= random.randint(10**2, 10**4)
    # xB= random.randint(10**2, 10**4)
    # yA = fastMulty(g, xA, p)
    # yB = fastMulty(g, xB, p)
    # print("yA = ", g, "^", xA," mod ", p," = ", yA)
    # print("yB = ", g, "^", xB," mod ", p," = ", yB)
    # Zab = fastMulty(yB, xA, p)
    # Zba = fastMulty(yA, xB, p)
    # print("Zab = ", yB, "^", xA," mod ", p," = ", Zab)
    # print("Zba = ", yA, "^", xB," mod ", p," = ", Zba)
    # print("Zab = Zba = ",Zba)
    ######################################################
    #                     4 часть                        #
    ###################################################### 
    # y = a^x mod p
    # y =  9
    # a = 2
    # p = random.randint(10**1, 10**2)
    # while not is_prime(p):
    #     p = random.randint(10**1, 10**2)
    # m, k = generate_m_k(p)
    # m  = 6
    # k = 4
    # p=23
    # print("p = ", p, "; m = ", m, "; k = ", k)
    # massM=[]
    # massK=[]
    # for i in range(0, m):
    #     resF = (a**i)*y % p
    #     massM.append(resF)
    # for j in range(1, k+1):
    #     resS = a**(j*m) % p
    #     massK.append(resS)
    # print(massM)
    # print(massK,"\n")

    # i,j = find_duplicate_elements(massM, massK ,a, p,y,m)
    # print("i = ",i,"; j = ",j, "\n")

    # print("a^(i*m) = a^j * y\n")
    # print(a, "^(", i, "*", m, ") = ",  (a**(i*m))%p) 
    # print(a, "^", j, " * ", y," = ", ((a**j)*y)%p)

    # print("\nx = i*m-j = ", i,"*",m, "-", j, " = ", i*m-j)
    

    # y = a^x mod p
    y =  9
    a = 2
    p = random.randint(10**1, 10**2)
    while not is_prime(p):
        p = random.randint(10**1, 10**2)
    m, k = generate_m_k(p)
    print("p = ", p, "; m = ", m, "; k = ", k)
    baby = {fastMulty(a, j, p) * y % p: j for j in range(m)}
    giant = [fastMulty(a, (m * i), p) for i in range(1, k + 1)]
    print("baby - ", baby)
    print("giant - ", giant)
    for i, el in enumerate(giant, 1):
        if (j := baby.get(el)) is not None:
            x = i * m - j
            break
        else:
            x = "Not found"
    print("a^(i*m) = a^j * y\n")
    print(a, "^(", i, "*", m, ") = ",  (a**(i*m))%p) 
    print(a, "^", j, " * ", y," = ", ((a**j)*y)%p)

    print("\nx = i*m-j = ", i,"*",m, "-", j, " = ", i*m-j)
    print(x)

if __name__ == "__main__":
    main()
