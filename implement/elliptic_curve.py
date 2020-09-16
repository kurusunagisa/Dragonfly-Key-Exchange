import math
import secrets

import numpy as np
from is_quadratic_residue import is_quadratic_residue
from sympy.ntheory.residue_ntheory import sqrt_mod


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
        raise Exception("modular inverse does not exist")
    return x % m


def TonelliShanks(a, p):
    return sqrt_mod(a, p)


"""
def TonelliShanks(a, p):
    S, Q = 1, 0
    while True:
        z = secrets.randbelow(p - 1) + 1
        if not is_quadratic_residue(z, p):
            break
    print(z)

    P = (p - 1) // 2
    while P % 2 == 0:
        S += 1
        P //= 2
    Q = P
    print(Q, S)

    M = S
    c = pow(z, Q, p)
    t = pow(a, Q, p)
    R = pow(a, (Q + 1) // 2, p)

    while True:
        if t == 0:
            return 0

        if t == 1:
            return R
        #i = 1
        t2=t
        for i in range(1, M):
            t2 = (t2 * t2) % p
            print(t2)
            if  t2 == 1:
                break
        print (i,M)

        b = pow(c * c, M - i - 1, p)
        M = i
        c = pow(b, 2, p)
        t = (t * c) % p
        R = (R * b) % p
"""


class ellipticCurve:
    def __init__(self, a, b, p, q=None):
        self.a = a
        self.b = b
        self.p = p
        self.q = q

    def __eq__(self, o):
        s = self
        if isinstance(s, ellipticCurve) and isinstance(o, ellipticCurve):
            return s.a == o.a and s.b == o.b and s.p == o.p
        return False

    # TODO: 平方余剰にする
    def yCalc(self, x):
        fx = (pow(x, 3, self.p) + self.a * x + self.b) % self.p
        return sqrt_mod(fx, self.p)


class ellipticCurvePoint:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

    def __eq__(self, b):
        a = self
        # print(a.x,a.y,b.x,b.y)
        if isinstance(a, ellipticCurvePoint) and isinstance(b, ellipticCurvePoint):
            if a.curve == b.curve:
                return a.x == b.x and a.y == b.y
        return False

    """
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
    """

    def isInfinity(self):
        return self.x == 0 and self.y == 0

    def add(self, p2):
        if self.isInfinity():
            return p2

        if p2.isInfinity():
            return self

        p1 = self
        p3 = ellipticCurvePoint(0, 0, self.curve)
        if p1.x == p2.x:
            λ = (
                (3 * (p1.x) ** 2 + self.curve.a) * modinv(2 * p1.y, self.curve.p)
            ) % self.curve.p
        else:
            λ = (((p2.y - p1.y) * modinv(p2.x - p1.x, self.curve.p))) % self.curve.p
        p3.x = (λ ** 2 - (p1.x + p2.x)) % self.curve.p
        p3.y = (λ * (p1.x - p3.x) - p1.y) % self.curve.p
        return p3

    def mul(self, n):
        R = ellipticCurvePoint(0, 0, self.curve)
        T = self
        while n > 0:
            if n & 1 == 1:
                R = R.add(T)
            n //= 2
            T = T.add(T)
        return R

    """
    def mul(self, n):
        P = self
        Q = self
        for i in range(1, n):
            P = P.add(Q)
        return P
    """

    def inverse(self):
        newpoint = ellipticCurvePoint(self.x, self.curve.p - self.y, self.curve)
        return newpoint


def test():
    a = 1
    b = 10
    p = 29
    curve = ellipticCurve(a, b, p)
    """
    P = ellipticCurvePoint(10, 37747, curve)
    R = ellipticCurvePoint(7, 12, curve)
    Q = ellipticCurvePoint(25, 21193, curve)
    assert Q.add(P) == R
    """
    # S = curve.yCalc(97)
    # print(type(S))
    # print(S)
    # return
    P = ellipticCurvePoint(10, 37747 % p, curve)
    R = ellipticCurvePoint(13, 25, curve)
    Q = P.add(P)
    assert Q.add(P) == R
    assert P.mul(3) == R
    assert P.times(3) == R
    print(P.mul(1000000))
    # assert P.add(P) == P.mul(2)


def main():
    test()
    exit(2)
    a = 1
    b = 6
    p = 11
    curve = ellipticCurve(a, b, p)
    # Y = ellipticCurve.yCalc(curve, n)
    # d = ellipticCurvePoint(n, Y, curve)
    # Y = ellipticCurve.yCalc(curve, l)
    # e = ellipticCurvePoint(l, Y, curve)
    d = ellipticCurvePoint(2, 7, curve)
    e = ellipticCurvePoint(2, 7, curve)
    # print(d.y % p)
    # print(e.y % p)
    # f = ellipticCurvePoint(0, 0, curve)
    f = d.add(e)
    print(f.x)
    print(f.y)
    g = f.add(d)
    print(g)
    P = ellipticCurvePoint(2, 7, curve)
    print(P.mul(4))


if __name__ == "__main__":
    test()
