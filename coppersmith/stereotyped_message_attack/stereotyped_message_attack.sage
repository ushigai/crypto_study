from Crypto.Util.number import *


class RSA:
    def __init__(self, bits):
        assert bits % 2 == 0
        self.gen_new_key(bits)
    
    def gen_new_key(self, bits):
        self.p = getPrime(bits // 2)
        self.q = getPrime(bits // 2)
        self.N = self.p * self.q
        self.e = 3
        phi = (self.p - 1) * (self.q - 1)
        self.d = inverse(self.e, phi)

    def encryption(self, m):
        if isinstance(m, str):
            m = bytes_to_long(m.encode("utf-8"))
        if isinstance(m, bytes):
            m = bytes_to_long(m)
        c = pow(m, self.e, self.N)
        return c

    def decryption(self, c):
        m = pow(c, self.d, self.N)
        m = long_to_bytes(m)
        return m
    
    def stereotyped_message_attack(self, prefix, c):
        PR.<x> = PolynomialRing(Zmod(self.N))
        f = (prefix + x)^self.e - c
        diff = f.small_roots()
        if len(diff):
            return long_to_bytes(int(diff[0]))
        else:
            return "not found..."


m = b"stereotyped_message_attack!!!"
prefix = b"Hello..."
m = bytes_to_long(m)
prefix = bytes_to_long(prefix) << (m.bit_length() + 1)

m += prefix

r = RSA(2048)

print(long_to_bytes(m))
cipher = r.encryption(m)
plane = r.decryption(cipher)

print("-*-*-*-*-*-*-*-*-*-*-")
print(r.stereotyped_message_attack(prefix, cipher))
print("-*-*-*-*-*-*-*-*-*-*-")

