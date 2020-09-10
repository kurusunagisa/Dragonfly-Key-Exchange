
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import secrets


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


def encrypt(key, data):
    iv = AES.get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    b_data = (data).encode()
    b_data += b'\x00' * (16 - (len(b_data) % 16))
    print("plain_text = ",b_data)
    ciphertext = cipher.encrypt(b_data)
    print("cipher_text = ",ciphertext)
    return ciphertext, iv


def decrypt(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC ,iv = iv)
    plaintext = cipher.decrypt(ciphertext)
    print("decrypted_text = ",plaintext)
    return plaintext


def main():
    key = get_random_bytes(16)
    data = "abcdfdsagasgsagassgas"
    ciphertext, iv = encrypt(key, data)
    plaintext = decrypt(key, ciphertext, iv)


if __name__ == "__main__":
    main()
