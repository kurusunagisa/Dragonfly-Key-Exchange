import secrets
import numpy as np
from elliptic_curve import ellipticCurve, ellipticCurvePoint
import hashlib

#peer_scalar 相手のスカラー
#peer_element 相手の要素
#private 自分の秘密鍵
#PE 共有点
#p macアドレス
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
    print(len("2531294081115351838688818799282891409517513240653165212510694309604509348519731245426893811242554901549455831447083505772980633097212593741993105765561347846"))
    #commit()


if __name__ == "__main__":
    main()
