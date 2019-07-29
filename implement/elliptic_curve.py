import numpy as np
import math as mt
import random as rd
import secrets as sc
import hashlib as hl

a = 10000000000000
b = 10000000000
p = 65537
n = sc.randbelow(10000)
l = sc.randbelow(10000)
password :bytes = 1234
k :bytes = 256
class ellipticCurve:
    def __init__(self):
        self.a = a
        self.b = b
        self.p = p

    def yCalc(self,x):
        return mt.sqrt(x ** 3 + self.a * x + self.b)

class ellipticCurvePoint:
    def __init__(self,x,y):
        self.x :int= x
        self.y :int= y


    def add(self, o, r,val):
        ram: float
        if o.x == r.x:
            ram = ((3 * o.y)**2 + val.a)/(2 * r.y)
        else:
            ram = ((r.y - o.y) / (r.x - o.x))
        self.x = ram ** 2 - (o.x + r.x)
        self.y :int= (-ram * (self.x - o.x) - o.y) % p

class Hash:

    def __init__(self, a, b, p):
        self.a = a

    def makeHash(a,b,password,counter):
        H = hl.shake_256()
        old = a + b + password + counter
        H.update(old)
        return H.hexdigest(256)


if __name__ == "__main__":
    val = ellipticCurve()
    Y = ellipticCurve.yCalc(val,n)
    d = ellipticCurvePoint(n, Y)
    Y = ellipticCurve.yCalc(val,l)
    e = ellipticCurvePoint(l,Y)
    print(d.y % p)
    print(e.y % p)
    f = ellipticCurvePoint(0,0)
    ellipticCurvePoint.add(f, d, e, val)
    print(f.y)