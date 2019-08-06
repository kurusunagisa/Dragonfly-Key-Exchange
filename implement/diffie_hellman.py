from elliptic_curve import ellipticCurve,ellipticCurvePoint
import sympy

def main():
    a = 1
    b = 10
    p = 29
    curve = ellipticCurve(a, b, p)
    G = ellipticCurvePoint(10, 37747, curve)

    da = 11
    Qa = G.mul(da)
    db = 9
    Qb = G.mul(db)

    Ka = Qb.mul(da)
    Kb = Qa.mul(db)
    print(Ka)
    print(Kb)

if __name__ == "__main__":
    main()
