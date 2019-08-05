from elliptic_curve import ellipticCurve, ellipticCurvePoint
import Hash
from KDF import kdf
import diffie_hellman
from is_quadratic_residue import is_quadratic_residue

def main():
    p = 29
    found = 0
    counter = 1
    base = Hash.main()
    print(base)
    temp = kdf(base, p)
    print(temp)
    seed = (temp % (p - 1)) + 1

if __name__ == "__main__":
    main()
