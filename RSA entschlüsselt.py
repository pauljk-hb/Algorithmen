import random

def RSA_verschlüsseln(p,q):
    n = p * q
    print("n: ", n)
    m = (p - 1) * (q - 1)
    print("m :", m)
    e=17
    print("e: ", e)
    d = pow(e,-1,m)
    d +=m
    print("d: ", d)
    return n,m,e,d

def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def get_prim():
    p = 0
    q = 0
    n = pow(10, 300) + 1
    while q == 0:
        prim = miller_rabin(n, 5)
        if prim:
            if p == 0:
                p = n
                print("p:", p)
            elif q == 0:
                q = n
                print("q:", q)
        n += 2
    return p, q


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1

def entschlusselung(rest):
    letters = []
    while rest > 1:
        rest, remainder = divmod(rest, 256) # Gibt den Rest zurück und den Quotienten, weil round/int ungenau gerundet hat
        letters.append(chr(remainder))
    return letters

verschluesselt = int(input("Zu Zahl eingeben: "))
p, q = get_prim()
n,m,e,d = RSA_verschlüsseln(p,q)
print(f"öffentlicher Schlüssel({n},{e})")
print(f"privater Schlüssel({n},{d})")
rsa_entschluesselt = pow(verschluesselt, d, n)
text = entschlusselung(rsa_entschluesselt)
print("Verschlüsselter Text:", listToString(text))
