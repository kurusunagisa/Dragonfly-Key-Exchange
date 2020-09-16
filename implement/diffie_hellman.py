from elliptic_curve import ellipticCurve,ellipticCurvePoint
import binascii

def main():
    curve = ellipticCurve(a=2, b=17, p=31)
    temp = 'D4-6D-6D-A0-96-B4'.replace('-', '')
    alice = binascii.unhexlify(temp)
    print(alice)
    temp = '00-FF-F4-EF-53-FE'.replace('-', '')
    bob = binascii.unhexlify(temp)
    print(bob)
    password = '123456'.encode()
    print(password)
    G = ellipticCurvePoint(10, 13, curve)
    da = 6
    Qa = G.mul(da)
    print(Qa)
    db = 23
    Qb = G.mul(db)

    Ka = Qb.mul(da)
    Kb = Qa.mul(db)
    print(Ka)
    print(Kb)


if __name__ == "__main__":
    main()
