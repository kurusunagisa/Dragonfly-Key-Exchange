import numpy as np
import math as mt
import random as rd
import secrets as sc
import hashlib as hl
import array as ar

a = 10000000000000
b = 10000000000
p = 65537
n = sc.randbelow(10000)
l = sc.randbelow(10000)
password :bytes = 1234
k: bytes = 256
alice = 0xFFFFF
bob = 0xDDDDDDD
class ellipticCurve:
    def __init__(self):
        self.a = a
        self.b = b
        self.p = p

    def yCalc(self,x):
        return mt.sqrt(x ** 3 + self.a * x + self.b)

class ellipticCurvePoint:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

    def tobin(self, n):
        list = []
        while 1:
            a = int(n % 2)
            #list.insert(0,a)
            list.append(a)
            if a == 1:
                n -= 1
            n /= 2
            #print(a)
            if n < 1:
                break
        return list


    def add(self, o, r,val):
        ram: float
        if o.x == r.x:
            ram = ((3 * o.y)**2 + val.a)/(2 * r.y)
        else:
            ram = ((r.y - o.y) / (r.x - o.x))
        self.x = int(ram ** 2 - (o.x + r.x))
        self.y = int((-ram * (self.x - o.x) - o.y) % p)

    def timesAdd(self, o, r,val):
        ram: float
        if o.x == r.x:
            ram = ((3 * o.y)**2 + val.a)/(2 * r.y)
        else:
            ram = ((r.y - o.y) / (r.x - o.x))
        return int((-ram * (self.x - o.x) - o.y) % p)

    def times(self, n, P):
        Q = 0
        #print(n)
        n_bin = ellipticCurvePoint.tobin(val, n)
        #print(n_bin)
        R = Q
        T = P
        for i in n_bin:
            #print(i)
            if i == 1:
                #楕円曲線上の加算しなきゃいけないなぁ…
                R += T
            T += T
            print(T)
        return R


class Hash:

    def __init__(self):
        self.a = alice
        self.b = bob
        self.p = p

    def makeHash(self,password,counter):
        old = str(self.a + self.b + password + counter)
        H = hl.sha3_512(old.encode()).hexdigest()
        return H

class keyDerivationFunction:

    def __init__(self):
        a = 1

    def dragonflyHuntingAndPecking(self):
        a = 1

    def KDF(self, base):
        a = 1



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
    R = ellipticCurvePoint.times(val, 115, f.y)
    print(R)

    counter = 2
    M = Hash()
    S = Hash.makeHash(M, password, counter)
    print(S)