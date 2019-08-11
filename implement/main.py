import diffie_hellman
from elliptic_curve import ellipticCurve, ellipticCurvePoint
from makeHash import Hash
from is_quadratic_residue import is_quadratic_residue, lsb
from KDF import dev


def main():
    diffie_hellman.main()

if __name__ == "__main__":
    PE = main()
