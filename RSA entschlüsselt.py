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
    return n,e,d

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
    n = pow(10, 300) + 1 # Bestimmt den Startwert und die länge der Primzahl
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


def listToString(s): # Macht aus dem Array ein String
    str1 = ""

    for ele in s:
        str1 += ele

    return str1

def entschlusselung(rest):
    letters = []
    while rest > 1:
        rest, remainder = divmod(rest, 256) # Gibt den Rest zurück und den Quotienten, weil round/int ungenau gerundet hat
        letters.append(chr(remainder)) # Bestimmt den Buchstaben/Zeichen und fügt es dem array hinzu
    return letters

verschluesselt = 663806463140071210056600843385572975928276241316455961262541230549457680980124545609765974897140035529952815801460129652934498844101862754571648662226863590522194004439190434259474804107950671684005006028169665657209499187898956151368172389829876603668927168324528065057877423157572650506358903437237634413034274786157178630258829604158108168884920866061998195120171076997276115380350681155064022769274950308504035521060246215507917198247624870144419171388079172216011738890290087337471642858931601393132154297632050982399589516128005526333681496947968937332043922938994400829785493176252466964678308
p, q = get_prim() # Primzahlen werden bestimmt
n,e,d = RSA_verschlüsseln(p,q) # Mit p und q wird das RSA-Modul (n), der private key (d) und der öffentliche key (e) zurückgegeben
print(f"öffentlicher Schlüssel({n},{e})")
print(f"privater Schlüssel({n},{d})")
rsa_entschluesselt = pow(verschluesselt, d, n) # Verschlüsselte Zahl wird mit privaten key (d) und RSA-Modul (n) entschlüsselt
text = entschlusselung(rsa_entschluesselt) # Wandelt Zahl wieder in Zeichen um
print("Verschlüsselter Text:", listToString(text))
