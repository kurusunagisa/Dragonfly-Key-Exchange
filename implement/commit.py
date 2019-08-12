import secrets
import numpy as np
from ECC import ECC
from elliptic_curve import ellipticCurve, ellipticCurvePoint
import hashlib


def commit():
    PE = ECC()
    q = 1863481
    a = 1
    b = 10
    p = 29
    sender_id :bytes= (0xFFFF).to_bytes(2, 'big')

    private, mask = secrets.randbelow(q - 1) + 1, secrets.randbelow(q - 1) + 1
    scalar = (private + mask) % q
    temp = PE.mul(mask)
    print(temp)
    Element = temp.inverse()
    print(private)
    print(Element)
    peer_scalar = 2
    curve = ellipticCurve(a, b, p)
    x = 5
    y = curve.yCalc(x)
    peer_element = ellipticCurvePoint(x, y, curve)
    ss = (PE.mul(peer_scalar).add(peer_element).mul(private)).x
    print(ss)
    p_len = len(list(map(int, format(p, "b"))))
    n=p_len * 2
    string = str(ss) + "Dragonfly Key Derivation"
    kck_mk = str(hashlib.shake_256(string.encode()).hexdigest(n))
    kck = kck_mk[0:p_len]
    mk = kck_mk[p_len:(p_len * 2)]
    print(kck)
    print(mk)

    return scalar, peer_scalar, Element, peer_element, kck

    #confirm = H(kck | scalar | peer-scalar | Element | Peer-Element | <sender-id>)

    #ss = F(scalar-op(private,element-op(peer-Element,scalar-op(peer-scalar, PE))))


def main():
    commit()


if __name__ == "__main__":
    main()
