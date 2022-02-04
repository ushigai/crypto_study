from Crypto.Util.number import *

class schmidt_samoa:
    def __init__(self, bits): # 初期化（鍵生成）
        self.gen_new_key(bits)

    def gen_new_key(self, bits): # 鍵生成
        self.p = getStrongPrime(bits)
        self.q = getStrongPrime(bits)
        self.N = self.p**2 * self.q
        lcm_pq = self.LCM(self.p - 1, self.q - 1)
        self.d = inverse(self.N, lcm_pq)

    def LCM(self, a, b): # a, bの最小公倍数を計算
        return (a * b) // GCD(a, b)

    def encryption(self, m): # 暗号化
        m = bytes_to_long(m.encode("utf-8"))
        c = pow(m, self.N, self.N)
        return c

    def decryption(self, c): # 復号
        m = pow(c, self.d, self.p * self.q)
        m = long_to_bytes(m).decode("utf-8")
        return m


r = schmidt_samoa(1024) # 1024bitの鍵を生成
m = "Hello_Schmidt_Samoa_cryptography!!!"
cipher = r.encryption(m)
print("cipher :", cipher)

plane = r.decryption(cipher)
print("plane :", plane)
