from Crypto.Util.number import *
from time import perf_counter as time

class Schmidt_Samoa: # Schmidt-Samoa暗号
    def __init__(self, bits):
        self.gen_new_key(bits)

    def gen_new_key(self, bits):
        self.p = getStrongPrime(bits)
        self.q = getStrongPrime(bits)
        self.N = self.p**2 * self.q
        lcm_pq = self.LCM(self.p - 1, self.q - 1)
        self.d = inverse(self.N, lcm_pq)

    def LCM(self, a, b):
        return (a * b) // GCD(a, b)

    def encryption(self, m):
        m = bytes_to_long(m.encode("utf-8"))
        c = pow(m, self.N, self.N)
        return c

    def decryption(self, c):
        m = pow(c, self.d, self.p * self.q) # ここの指数計算が遅いと考えられる
        m = long_to_bytes(m).decode("utf-8")
        return m

class RSA: # RSA暗号
    def __init__(self, bits):
        self.gen_new_key(bits)

    def gen_new_key(self, bits):
        self.p = getStrongPrime(bits)
        self.q = getStrongPrime(bits)
        self.N = self.p * self.q
        self.e = 65537
        phi = (self.p - 1) * (self.q - 1)
        self.d = inverse(self.e, phi)

    def encryption(self, m):
        m = bytes_to_long(m.encode("utf-8"))
        c = pow(m, self.e, self.N)
        return c

    def decryption(self, c):
        m = pow(c, self.d, self.N)
        m = long_to_bytes(m).decode("utf-8")
        return m


bits = 1024
m = "Hello_Schmidt_Samoa_cryptography!!!"
count = 1000 # 指数計算を行う回数

r1 = Schmidt_Samoa(bits)
cipher = r1.encryption(m)
plane = r1.decryption(cipher)
assert plane == m # 念のため正しく復号できることを確認
t0 = time()
for i in range(count):
    cipher = r1.encryption(m) # 暗号化

print("Schmidt-Samoa :", time() - t0, "[s]")

r2 = RSA(bits)
cipher = r2.encryption(m)
plane = r2.decryption(cipher)
assert plane == m # 念のため正しく復号できることを確認
t0 = time()
for i in range(count):
    cipher = r2.encryption(m) # 暗号化

print("RSA :", time() - t0, "[s]")

