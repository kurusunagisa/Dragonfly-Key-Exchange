import hashlib
import hmac

def confirm(scalar, peer_scalar, Element, peer_element, kck,sender_id):
    b_scalar = scalar.to_bytes(4, 'big')
    b_peerscalar = peer_scalar.to_bytes(3, 'big')
    b_element = abs(Element.x).to_bytes(4, 'big')
    b_peerelement = abs(peer_element.x).to_bytes(3, 'big')
    c_kck = chr(int(kck, 16)).encode()
    base = c_kck + b_scalar + b_peerscalar + b_element + b_peerelement + sender_id

    confirm = hashlib.sha3_512(base).hexdigest()

    #print(confirm)


    return confirm

def main(scalar, peer_scalar, Element, peer_element, kck):
    confirm(peer_scalar, Element, peer_element, kck)

if __name__ == "__main__":
    main()