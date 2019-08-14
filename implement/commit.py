import secrets
import numpy as np
from ECC import ECC
from elliptic_curve import ellipticCurve, ellipticCurvePoint
import hashlib

#peer_scalar 相手のスカラー
#peer_element 相手の要素
#p
def commit(peer_scalar, peer_element, private, PE, p):

    ss = (PE.mul(peer_scalar).add(peer_element).mul(private)).x
    print(ss)
    p_len = len(list(map(int, format(p, "b"))))
    n = p_len * 2
    string = str(ss) + "Dragonfly Key Derivation"
    kck_mk = str(hashlib.shake_256(string.encode()).hexdigest(n))
    kck = kck_mk[0:p_len]
    mk = kck_mk[p_len:(p_len * 2)]
    print(kck)
    print(mk)

    return kck, mk

    # confirm = H(kck | scalar | peer-scalar | Element | Peer-Element | <sender-id>)

    #ss = F(scalar-op(private,element-op(peer-Element,scalar-op(peer-scalar, PE))))


def main():
    commit()


if __name__ == "__main__":
    main()
