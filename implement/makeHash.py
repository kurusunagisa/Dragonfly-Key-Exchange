import hashlib


class Hash:
    def __init__(self, alice: bytes, bob: bytes, password: bytes):
        self.a = alice
        self.b = bob
        self.password = password


    def makeHash(self, counter):
        #print(type(counter))
        old = str(max(self.a, self.b) + min(self.a, self.b) + self.password + chr(counter).encode())
        #print(old)
        H = hashlib.sha3_512(old.encode()).hexdigest()
        return H


def main():
    alice = 0xFFFFF.to_bytes(3, 'big')
    bob = 0xDDDDDDD.to_bytes(4, 'big')
    password = int(1234).to_bytes(2, 'big')
    counter = 1
    M = Hash(alice, bob, password)
    S = M.makeHash(counter)
    print(S)
    return S


if __name__ == "__main__":
    main()