import random

def RSA_verschlüsseln(p,q):
    n = p * q
    print("n: ", n)
    m = (p - 1) * (q - 1)
    print("m :", m)
    e=17
    print("e: ", e)
    d=inverse(e,m)
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

def verschlusseln(wort):
    buchstaben_array = []
    for buchstabe in wort:
        buchstaben_array.append(buchstabe)

    ergebnis = 0
    for j in range(len(buchstaben_array)):
        asciNumber = ord("" + buchstaben_array[j])
        ergebnis = ergebnis + ((asciNumber) * 256 ** j)
    return ergebnis

def inverse(a, m):
    r = [a, m]
    q = [0, a // m]
    x = [1, 0]
    k = 0
    while True:
        r = r + [r[k] % r[k + 1]]
        if r[k + 2] == 0:
            x = x + [x[k] - q[k + 1] * x[k + 1]]
            break
        q = q + [r[k + 1] // r[k + 2]]
        x = x + [x[k] - q[k + 1] * x[k + 1]]
        k += 1
    return x[k + 1]

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

text = str(input("Zu verschlüsselnen Text eingeben: "))
p, q = get_prim()
n,m,e,d = RSA_verschlüsseln(p,q)
print(f"öffentlicher Schlüssel({n},{e})")
print(f"privater Schlüssel({n},{d})")
verschlusselteZahl = verschlusseln(text)
rsa_verschluesselt = pow(verschlusselteZahl,e, n)

print("Verschlüsselter Text:", rsa_verschluesselt)
