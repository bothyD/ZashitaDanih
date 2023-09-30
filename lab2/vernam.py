import random

def xor(a, b):
    return (a and not b) or (not a and b)

def xor_str(str1, str2):
    res = ""
    for i in range(8):
        if xor(int(str1[i]), int(str2[i])):
            res+="1"
        else:
            res+="0"
    return res

def vernam():
    sicret_posl = "HELLO"
    n = len(sicret_posl)
    sicret_posl_bin = []
    sicret_key_bin = []
    for char in sicret_posl:
        sicret_posl_bin.append( bin(ord(char))[2:].zfill(8))
        random_byte = random.randint(0, 255)
        random_byte_str = format(random_byte, '08b')
        sicret_key_bin.append(random_byte_str)
    res = []
    for i in range(n):
        res.append(xor_str(sicret_posl_bin[i], sicret_key_bin[i]))
    print("send: ", sicret_posl_bin)
    print("key: ", sicret_key_bin)
    print("\nshifr = send xor key = ", res)

    sicret_posl_bin2 = []
    for i in range(n):
        sicret_posl_bin2.append(xor_str(res[i], sicret_key_bin[i]))
    print("deshifr = shifr xor key = ", sicret_posl_bin2)
    for el in sicret_posl_bin2:
        char = chr(int(el, 2))
        print(char, end="")

   