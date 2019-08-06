from secrets import choice
from sympy.ntheory import sqrt_mod


def lgr(a, p):
    return sqrt_mod(a, p)


def lsb(n):
    return n & 1


def findqr(p):
    while True:
        qr = choice(range(1, p-1))
        if lgr(qr, p) == 1:
            return qr


def findqnr(p):
    while True:
        qnr = choice(range(1, p-1))
        if lgr(qnr, p) == 1:
            return qnr


def is_quadratic_residue(val, p):
    qr = findqr(p)
    qnr = findqnr(p)
    r = (choice(range(1, p-1))) + 1
    num = (val * r * r) % p
    if (lsb(r) == 1):
        num = (num * qr) % p
        if lgr(num, p) == 1:
            return True
    else:
        num = (num * qnr) % p
        if lgr(num, p) == 1:
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
