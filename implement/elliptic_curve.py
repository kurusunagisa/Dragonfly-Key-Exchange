import numpy as np
import math as mt
import random as rd
import secrets as sc

a = 10000000000000
b = 10000
p = 65537

def ellipticCurve(x):
    y = mt.sqrt(x ** 3 + a * x + b) % p
    return y

def primeNumber(n):
    return sc.randbelow(n)


if __name__ == "__main__":
    n = 56636
    prime = primeNumber(n)
    print(prime)

    Y = ellipticCurve(prime)
    print(round(Y))