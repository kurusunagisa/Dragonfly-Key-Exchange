from elliptic_curve import ellipticCurve,ellipticCurvePoint
import sympy
from ECC import ECC

def main():
    G = ECC()
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
