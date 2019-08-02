import numpy as np
import math
import secrets
import hashlib

password: bytes = 1234
alice = 0xFFFFF
bob = 0xDDDDDDD
# & 1をとればlsbがとれる
# TODO:逆元を求める関数をつくる

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def lgr(a, p):
    return pow(a, (p - 1) // 2, p)

def lsb(n):
    return n & 1

class ellipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    # TODO: 平方余剰にする
    def yCalc(self, x):
        return math.sqrt(x ** 3 + self.a * x + self.b)


class ellipticCurvePoint:

    def __init__(self, x, y, curve):
        self.x = int(x)
        self.y = int(y)
        self.curve = curve

    def __str__(self):
        return "(%d,%d)" % (self.x,self.y)

    def tobin(self, n):
        list = []
        while 1:
            a = int(n % 2)
            # list.insert(0,a)
            list.append(a)
            if a == 1:
                n -= 1
            n /= 2
            # print(a)
            if n < 1:
                break
        return list

    def add(self, p2):
        p1 = self
        p3 = ellipticCurvePoint(0, 0, curve)
        if p1.x == p2.x:
            λ = (((3 * p1.y)**2 + self.curve.a) * modinv(2 * p2.y, p)) % p
        else:
            λ = (((p2.y - p1.y) * modinv(p2.x - p1.x, p))) % p
        p3.x = int(λ**2 - (p1.x + p2.x)) % p
        p3.y = int((λ * (p1.x - p3.x) - p1.y) % p)
        return p3

    # TODO:Pを楕円曲線上の点にする
    """
    def times(self, n, P):
        Q = 0
        # print(n)
        n_bin = ellipticCurvePoint.tobin(curve, n)
        # print(n_bin)
        R = Q
        T = P
        for i in n_bin:
            # print(i)
            if i == 1:
                T = T.add(R)
            print(T)
        return R
    """
    def mul(self, n):
        P = self
        Q = self
        for i in range(1,n):
            P = P.add(Q)
        return P

class Hash:

    def __init__(self):
        self.a = alice
        self.b = bob
        self.p = p

    def makeHash(self, password, counter):
        old = str(self.a + self.b + password + counter)
        H = hashlib.sha3_512(old.encode()).hexdigest()
        return H


class keyDerivationFunction:

    def __init__(self):
        a = 1

    def dragonflyHuntingAndPecking(self):
        a = 1

    def KDF(self, base):
        a = 1


if __name__ == "__main__":
    a = 1
    b = 6
    p = 11
    curve = ellipticCurve(a, b, p)
    #Y = ellipticCurve.yCalc(curve, n)
    #d = ellipticCurvePoint(n, Y, curve)
    #Y = ellipticCurve.yCalc(curve, l)
    #e = ellipticCurvePoint(l, Y, curve)
    d = ellipticCurvePoint(2, 7, curve)
    e = ellipticCurvePoint(2, 7, curve)
    print(d.y % p)
    print(e.y % p)
    #f = ellipticCurvePoint(0, 0, curve)
    f = d.add(e)
    print(f.x)
    print(f.y)
    g = f.add(d)
    print(g)
    P = ellipticCurvePoint(2, 7, curve)
    print(P.mul(4))
    #R = ellipticCurvePoint.times(curve, 115, P)
    # print(R)

    counter = 2
    M = Hash()
    S = Hash.makeHash(M, password, counter)
    # print(S)
