
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


'''
class AESCipher(object):
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw)

    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(enc)

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
'''
def encrypt(key,string):
    cipher = AES.new(key, AES.MODE_CBC)
    string = ("abcd").encode()
    string += b'\x00' * (16 - (len(string) % 16))
    print(string)
    ciphertext = cipher.encrypt(string)
    print(ciphertext)


def main():


if __name__ == "__main__":
    main()