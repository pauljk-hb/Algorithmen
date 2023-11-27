import random

def RSA_verschlüsseln(p,q):
    n = p * q # RSA-Modul wird berechnet
    print("n: ", n)
    m = (p - 1) * (q - 1) # phi(m) wird berechnet. Euler-Fermat Satz
    print("m :", m)
    e=17 # e wird festgelegt
    print("e: ", e)
    d = pow(e,-1,m) # die inverse wird berechnet, um d (Privaten Key) zu bestimmen
    d +=m # verhindert, dass d negativ wird
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
        buchstaben_array.append(buchstabe) # Wort wird in buchstaben aufgeteilt und in das Array gesteckt

    ergebnis = 0
    for j in range(len(buchstaben_array)): # For schleife geht durch das Array
        asciNumber = ord("" + buchstaben_array[j])  # Die ASCII Nummer wird bestimmt
        ergebnis = ergebnis + ((asciNumber) * 256 ** j) # Die ASCII Nummer wird mit der Basis 256 berechnet
    return ergebnis

def get_prim():
    p = 0
    q = 0
    n = pow(10, 300) + 1 # Bestimmt den Startwert und länge der Primzahl
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

text = str(input("Zu verschlüsselnen Text eingeben: ")) # Text zum verschlüsseln wird eingelesen
p, q = get_prim() # Primzahlen werden bestimmt
n,m,e,d = RSA_verschlüsseln(p,q) # Mit p und q wird das RSA-Modul, der private key, Phi(m) und n returned
print(f"öffentlicher Schlüssel({n},{e})")
print(f"privater Schlüssel({n},{d})")
verschlusselteZahl = verschlusseln(text) # Wandelt den Text in eine Zahl
rsa_verschluesselt = pow(verschlusselteZahl,e, n) # Verschlüsselt die ASCII nummer mit dem öffentlichen Key aus dem RSA-Modul

print("Verschlüsselter Text:", rsa_verschluesselt)
