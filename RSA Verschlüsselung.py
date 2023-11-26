import random

def RSA_verschlüsseln(p,q, char):
    n = p * q
    print("n: ", n)
    m = (p - 1) * (q - 1)
    print("m :", m)
    #e = teilerfremd(m)
    e=65537
    print("e: ", e)
    d=inverse(e,m)
    print("d: ", d)
    return pow(char, e, n)

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

def teilerfremd(a):
    for i in range(3,a):
        if a%i==1: return i

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
    n = pow(10, 299) + 1
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
#p, q = get_prim()
p=11
q=13
cyperArray = []
for char in text:
    cyperArray.append(RSA_verschlüsseln(p,q,ord(char)))

print("Verschlüsselter Text:", cyperArray)
