import numpy as np
import math as mt

a = 10000000000000
b = 10000
p = 65537

def ellipticCurve(x):
    y = mt.sqrt(x ** 3 + a * x + b) % p
    return y


if __name__ == "__main__":
    i :float = 0.1
    for i in range(100):
        S = ellipticCurve(i)
        print(S)

