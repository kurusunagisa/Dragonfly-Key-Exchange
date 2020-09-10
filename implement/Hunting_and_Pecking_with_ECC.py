from elliptic_curve import ellipticCurve, ellipticCurvePoint
from makeHash import Hash
from is_quadratic_residue import is_quadratic_residue, lsb
from KDF import dev


def hunting_and_pecking_with_ecc(curve,alice,bob,password):
    k = 40
    found = 0
    counter = 1
    x = 0
    save = 0
    M = Hash(alice, bob, password)

    while True:
        base = M.makeHash((counter))
        #assert(type(base) == str)
        temp = int(dev(base, curve.p), 16)
        #assert(type(temp) == int)
        seed = (temp % (curve.p - 1)) + 1
        #assert (type(seed) == int)
        base = int(base, 16)
        if is_quadratic_residue((pow(seed,3,curve.p) + curve.a * seed + curve.b) % curve.p, curve.p):
            x = seed
            save = base
            break
        counter += 1
        counter %= 256
        if counter > k:
            break
        assert(found == 0 and counter <= k)
    #assert(curve.a == a and curve.b == b and curve.p == p)
    y = curve.yCalc(x)
    assert(type(save) == type(y))
    if lsb(y) == lsb(save):
        PE = ellipticCurvePoint(x, y, curve)
        #print("lsb(y) == lsb(save)",int(pow(x,3,curve.p) + curve.a * x + curve.b) % curve.p == pow(y,2,curve.p) % curve.p)
    else:
        PE = ellipticCurvePoint(x, curve.p - y, curve)
       #print("lsb(y) != lsb(save)", (pow(x,3,p) + (a * x) % p + b) % p == pow(y,2,p))
    #print(curve.yCalc(x) == y)
    print("PE",PE)
    return PE

def main():
    PE = ECC()
    print(PE)

if __name__ == "__main__":
    main()