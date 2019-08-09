from elliptic_curve import ellipticCurve, ellipticCurvePoint
from Hash import Hash
from KDF import dev
import diffie_hellman
from is_quadratic_residue import is_quadratic_residue, lsb


def main():
    a = 1
    b = 10
    p = 29
    alice = 0xFFFFF2131
    bob = 0xDDDDDDD
    password: bytes = 12345678
    k = 100000
    found = 0
    counter = 1
    x = 0
    save = 0
    M = Hash(alice, bob, password)
    print(type(M))

    while True:
        base = M.makeHash(counter)
        #assert(type(base) == str)
        temp = int(dev(base, p), 16)
        #assert(type(temp) == int)
        seed = (temp % (p - 1)) + 1
        #assert (type(seed) == int)
        base = int(base, 16)
        if is_quadratic_residue((pow(seed,3,p) + a * seed + b) % p, p):
            #if found == 0:
            x = seed
            save = base
            break
        counter += 1
        if counter > k:
            break
        assert(found == 0 and counter <= k)

    curve = ellipticCurve(a, b, p)
    assert(curve.a == a and curve.b == b and curve.p == p)
    y = int(curve.yCalc(x))
    assert(type(save) == type(y))
    if lsb(y) == lsb(save):
        PE = ellipticCurvePoint(x, y, curve)
        print("lsb(y) == lsb(save)",int(pow(x,3,p) + a * x + b) == y** 2)
    else:
        PE = ellipticCurvePoint(x, p - y, curve)
        print("lsb(y) != lsb(save)", int(pow(x,3,p) + a * x + b) == y**2)
    #print(curve.yCalc(x) == y)
    print(PE.y)
    return PE


if __name__ == "__main__":
    PE = main()
