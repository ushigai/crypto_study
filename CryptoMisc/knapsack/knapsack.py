from Crypto.Util.number import *
from random import getrandbits


class knapsack:
    def __init__(self, bits): # 初期化（鍵生成）
        self.gen_new_key(bits)
    
    def gen_new_key(self, bits): # 鍵生成の関数
        self.A = []
        a, b = 0, 0
        for _ in range(bits): # 超増加数列Aを生成
            a += getrandbits(32) + b
            b += a # 変数bにこれまでの数列の総和を代入しAが超増加になるようにする
            self.A.append(a)
            
        # 互いに素になるように素数で秘密鍵を定義
        self.q = getPrime(1024)
        self.p = getPrime(1024)
        
        assert self.q > sum(self.A) # 法qを上回ってないか確認

        self.pub_key = [a * self.p % self.q for a in self.A] # 公開鍵を生成
        f = open("pub_key.py", "w")
        f.write("pub_key = " + str(self.pub_key) + "\n")
        f.close()

    def encryption(self, m): # 暗号化の関数
        m = bytes_to_long(m.encode("utf-8"))
        m = bin(m)[2:]
        length = len(m)
        cipher = sum([int(m[i]) * self.pub_key[i] for i in range(length)]) # 平文と秘密鍵のベクトルから暗号文（ベクトル内積）を計算
        f = open("cipher.py", "w")
        f.write("cipher = " + str(cipher) + "\n")
        f.close()
        return cipher

    def decryption(self, c): # 復号の関数
        c = c * inverse(self.p, self.q) % self.q
        m = ""
        for a in self.A[::-1]: # Aが超増加数列であることを利用し復号
            if a <= c:
                c -= a
                m += "1"
            else:
                m += "0"
        m = long_to_bytes(int(m[::-1], base=2)).decode("utf-8")
        return m


plane = "Hello!!! HM-knapsack cryptography!!!"
length = bytes_to_long(plane.encode("utf-8")).bit_length()
print("bit length :", length)

r = knapsack(length) # 鍵長は平文のbit長分必要なのでlength分生成

cipher = r.encryption(plane)
print("cipher :", cipher)

plane = r.decryption(cipher)
print("plane :", plane)
