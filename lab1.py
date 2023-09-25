import random
import math
import numpy
### y = a^x mod p.

def fastMulty(a, x, p):
    y = 1
    s = a
    for i in range(len(x)):
        if x[i]==1:
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
    return U 


def binNum(x):
    mas = []
    last_bit = 0
    while x != 0:
        last_bit = x & 1
        mas.append(last_bit)
        x = x >> 1
    print()
    return mas

def is_prime(p):
    if p <= 1:
        return False
    b = int(math.sqrt(p))
    for i in range(2, b+1):
        if p % i == 0:
            return False
    return True

def find_duplicate_elements(array1, array2):
    for element1 in array1:
        for element2 in array2:
            if element1 == element2:
                i = array1.index(element1)
                j = array2.index(element2)
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
    # masBin = binNum(x)
    # res = fastMulty(a, masBin, p)
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
    # q = 0
    # p = 0
    # go = True
    # while go:
    #     q = random.randint(10**2, 10**4)
    #     while not is_prime(q):
    #         q = random.randint(10**6, 10**9)
    #     p = 2*q + 1
    #     if is_prime(p):
    #         go = False
    # print(q, p)

    # i = 2
    # masBin = binNum(q)
    # while i != p-2:
    #     g = fastMulty(i, masBin, p)
    #     if g != 1:
    #         break
    #     i+=1
    # print(g)
    # xA= 131
    # xB= 111
    # masBinA = binNum(xA)
    # masBinB = binNum(xB)
    # yA = fastMulty(g, masBinA, p)
    # yB = fastMulty(g, masBinB, p)
    # print("yA = ", yA, " yB = ",yB)

    # Zab = fastMulty(yB, masBinA, p)
    # Zba = fastMulty(yA, masBinB, p)
    # print("Zab = ", Zab, " Zba = ",Zba)
    ######################################################
    #                     4 часть                        #
    ###################################################### 
    #y = a^x mod p
    y =  9
    a = 2
    p =23
    pSqr = int(p**(-2))

    m = 6
    k =4

    massM=[]
    massK=[]
    for i in range(0, m):
        resF = (a**i)*y % p
        massM.append(resF)
    for j in range(1, k+1):
        resS = a**(j*m) % p
        massK.append(resS)
    print(massM)
    print(massK)

    i,j = find_duplicate_elements(massM, massK)
    print(i,j)
    print((a**(i*m))%p, " ", ((a**(j+1))*y)%p)

    print("x = ", i*m - j)
 
if __name__ == "__main__":
    main()
