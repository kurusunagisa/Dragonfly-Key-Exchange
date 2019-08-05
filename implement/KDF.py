import hashlib

def kdf(base,p):
    n = len(list(map(int,format(p,"b"))))+ 64
    string = base + "Dragonfly Hunting And Pecking"
    H = int(hashlib.shake_256(string.encode()).hexdigest(n),16)
    print(H)
    return H

def main(base,p):
    H = kdf(base, p)
    #S = int(H)
    print(H)
    #S :int = H.format(int)
    #print(type(S))
if __name__ == "__main__":
    base = 'faaaaaa'
    p = 27
    main(base,p)