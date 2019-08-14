
#from diffie_hellman import diffie_hellman
from elliptic_curve import ellipticCurve, ellipticCurvePoint
from Hunting_and_Pecking_with_ECC import hunting_and_pecking_with_ecc
import binascii
from handshake import createPrivateAndMask
import hashlib
import math
from confirm import confirm


def main():
    curve = ellipticCurve(a=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
    b=0x0051953EB9618E1C9A1F929A21A0B68540EEA2DA725B99B315F3B8B489918EF109E156193951EC7E937B1652C0BD3BB1BF073573DF883D2C34F1EF451FD46B503F0, p=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, q=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA51868783BF2F966B7FCC0148F709A5D03BB5C9B8899C47AEBB6FB71E91386409
    )
    temp = 'D4-6D-6D-A0-96-B4'.replace('-', '')
    alice = binascii.unhexlify(temp)
    print(alice)
    temp = '00-FF-F4-EF-53-FE'.replace('-', '')
    bob = binascii.unhexlify(temp)
    print(bob)
    password = '123457'.encode()
    print(password)
    PE = hunting_and_pecking_with_ecc(curve, alice, bob, password)
    alice_scalar, alice_element, alice_private = createPrivateAndMask(PE)
    bob_scalar, bob_element, bob_private = createPrivateAndMask(PE)
    #ellipticCurvePoint(10, 13, curve)
    #ここから鍵交換プロトコルを使う
    temp1 = PE.mul(bob_scalar)
    temp2 = temp1.add(bob_element)
    temp3 = temp2.mul(alice_private)
    print(temp1, temp2, temp3)
    alice_ss = (temp3.x).to_bytes(math.ceil(math.log2(temp3.x) / 8),'big')
    #alice_ss = hex((PE.mul(bob_scalar).add(bob_element).mul(alice_private)).x)
    print(alice_ss)
    temp1 = PE.mul(alice_scalar)
    temp2 = temp1.add(alice_element)
    temp3 = temp2.mul(bob_private)
    print(temp1, temp2, temp3)
    bob_ss = (temp3.x).to_bytes(math.ceil(math.log2(temp3.x) / 8),'big')
    print(bob_ss)

    # commit
    ## alice
    n = len(list(map(int, format(PE.curve.p, "b")))) * 2
    temp = hashlib.shake_256(alice_ss + b'Dragonfly Key Derivation').hexdigest(512)
    alice_kck = temp[0:256]
    alice_mk = temp[256:512]
    print("alice_kck =", alice_kck)
    print("alice_mk =", alice_mk)
    ## bob
    temp = hashlib.shake_256(bob_ss + b"Dragonfly Key Derivation").hexdigest(512)
    bob_kck = temp[0:256]
    bob_mk = temp[256:512]
    print("bob_kck =", bob_kck)
    print("bob_mk =", bob_mk)


    #交換する前に自分のconfirmの値を求める
    ##alice側
    alice_confirm = confirm(alice_scalar, bob_scalar, alice_element, bob_element, alice_kck, alice)
    ##bob側
    bob_confirm = confirm(bob_scalar, alice_scalar, bob_element, alice_element, bob_kck, bob)
    #交換して，相手のconfirmの値が正しいか検証する
    ##alice側
    bob_confirm_expected = confirm(bob_scalar, alice_scalar, bob_element, alice_element, bob_kck, bob)
    ##bob側
    alice_confirm_expected = confirm(alice_scalar, bob_scalar, alice_element, bob_element, alice_kck, alice)

    #それぞれで計算結果と送られてきた結果を比較
    ##alice側
    if bob_confirm == bob_confirm_expected:
        print("alice: confirm successed")

    ##bob側
    if alice_confirm == alice_confirm_expected:
        print("bob: confirm successed")

if __name__ == "__main__":
    PE = main()
