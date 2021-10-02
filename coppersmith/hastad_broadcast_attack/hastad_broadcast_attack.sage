from Crypto.Util.number import *
from random import getrandbits


class RSA:
    def __init__(self, bits):
        self.A, self.B = [], [] # padding number
        self.N = [] # public key
        assert bits % 2 == 0
        self.bits = bits // 2
    
    def gen_new_key(self):
        self.p = getPrime(self.bits)
        self.q = getPrime(self.bits)
        self.ni = self.p * self.q
        self.N.append(self.ni)
        self.e = 5
        phi = (self.p - 1) * (self.q - 1)
        self.d = inverse(self.e, phi)

    def encryption(self, m):
        c = pow(m, self.e, self.ni)
        return c
    
    def padding(self, m, bits):
        a, b = getrandbits(bits), getrandbits(bits)
        self.A.append(a)
        self.B.append(b)
        m = a * m + b
        return m
    
    def HastadBroadcastAttack(self, dig, ciphers):
        F.<x> = PolynomialRing(Zmod(prod(self.N)), implementation='NTL')
        
        H = []
        for i in range(dig):
            h = (self.A[i]*x + self.B[i])^e - ciphers[i]
            h *= inverse_mod(int(h.lc()), self.N[i])
            H.append(h)

        # find coefficient T
        T = []
        for i in range(dig):
            mat = [0] * dig
            mat[i] = 1
            t = CRT(mat, self.N)
            T.append(t)

        g = sum([t * h for t, h in zip(T, H)])
        roots = g.small_roots()
        if len(roots):
            return long_to_bytes(int(roots[0]))
        else:
            return "Not found..."


bits = 2048
dig = 5
r = RSA(bits)

m = bytes_to_long(b"Hastad_Broadcast_attack!!!!!!!!")
ciphers = []

for i in range(dig):
    r.gen_new_key()
    cipher = r.encryption(r.padding(m, 512))
    ciphers.append(int(cipher))

print(r.HastadBroadcastAttack(dig, ciphers))
