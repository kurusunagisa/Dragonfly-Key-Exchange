import numpy as np
import math
import secrets


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





class ellipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def __eq__(self, o):
        s = self
        if isinstance(s, ellipticCurve) and isinstance(o, ellipticCurve):
            return s.a == o.a and s.b == o.b and s.p == o.p
        return False

    # TODO: 平方余剰にする
    def yCalc(self, x):
        return (math.sqrt(pow(x,3,self.p) + self.a * x + self.b)) % self.p


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

    '''
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
    '''

    def add(self, p2):
        p1 = self
        p3 = ellipticCurvePoint(0, 0, self.curve)
        if p1.x == p2.x:
            λ = ((3 * (p1.x)**2 + self.curve.a) *
                 modinv(2 * p1.y, self.curve.p)) % self.curve.p
        else:
            λ = (((p2.y - p1.y) * modinv(p2.x - p1.x, self.curve.p))) % self.curve.p
        p3.x = (λ**2 - (p1.x + p2.x)) % self.curve.p
        p3.y = (λ * (p1.x - p3.x) - p1.y) % self.curve.p
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
        for i in range(1, n):
            P = P.add(Q)
        return P


def test():
    a = 1
    b = 10
    p = 29
    curve = ellipticCurve(a, b, p)
    '''
    P = ellipticCurvePoint(10, 37747, curve)
    R = ellipticCurvePoint(7, 12, curve)
    Q = ellipticCurvePoint(25, 21193, curve)
    assert Q.add(P) == R
    '''
    P = ellipticCurvePoint(10, 37747, curve)
    R = ellipticCurvePoint(13, 25, curve)
    Q = P.add(P)
    assert Q.add(P) == R
    assert P.mul(3) == R
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
    main()