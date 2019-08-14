from elliptic_curve import ellipticCurve, ellipticCurvePoint
import secrets
#PE.curve
def createPrivateAndMask(PE):

    private = secrets.randbelow(PE.curve.q - 2) + 2
    mask    = secrets.randbelow(PE.curve.q - 2) + 2
    print("mask = ",mask)
    scalar  = (private + mask) % PE.curve.q


    temp = PE.mul(mask)
    print("temp =",temp)
    Element = temp.inverse()
    print("private =",private)
    print("Element =", Element)
    print("scalar =",scalar)
    return scalar, Element ,private


def handshake():

    scalar,Element,private = createPrivateAndMask(PE)

    sA, sB, eA, eB, kck,private = commit(peer_scalar,peer_element,private,PE,p)
    check1 = confirm(sA, sB, eA, eB, kck)
    check2 = confirm(sB,sA,eB,eA,kck)

def main():
    handshake()


if __name__ == "__main__":
    main()
