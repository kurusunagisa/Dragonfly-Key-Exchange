import hashlib


class Hash:
    def __init__(self, alice, bob, password):
        self.a = alice
        self.b = bob
        self.password = password

    def makeHash(self, counter):
        old = str(max(self.a, self.b) + min(self.a,
                                            self.b) + self.password + counter)
        H = hashlib.sha3_512(old.encode()).hexdigest()
        return H


def main():
    alice = 0xFFFFF
    bob = 0xDDDDDDD
    password: bytes = 1234
    counter = 1
    M = Hash(alice, bob, password)
    S = M.makeHash(counter)
    #print(S)
    return S


if __name__ == "__main__":
    main()
