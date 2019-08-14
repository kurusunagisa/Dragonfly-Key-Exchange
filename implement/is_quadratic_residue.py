import secrets

from sympy.ntheory import legendre_symbol


def lgr(a, p):
    return legendre_symbol(a, p)


def lsb(n):
    return n & 1

def rand(min,max):
    while True:
        r = secrets.randbits(max.bit_length())
        if min <= r < max:
            return r

def findqr(p):
    while True:
        qr = rand(1,p)
        if lgr(qr, p) == 1:
            return qr


def findqnr(p):
    while True:
        qnr = rand(1,p)
        if lgr(qnr, p) == -1:
            return qnr

#val 判断したいもの
def is_quadratic_residue(val, p):
    qr = findqr(p)
    qnr = findqnr(p)
    r = rand(2,p)
    num = (val * r * r) % p
    if (lsb(r) == 1):
        num = (num * qr) % p
        if lgr(num, p) == 1:
            return True
    else:
        num = (num * qnr) % p
        if lgr(num, p) == -1:
            return True
    return False


def main():
    p = 29
    val = 21
    #N = lgr(val,p)
    N = is_quadratic_residue(val, p)
    print(N)


if __name__ == "__main__":
    main()
