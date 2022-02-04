from Crypto.Util.number import *
from math import log2
from pub_key import pub_key
from cipher import cipher


def create_matrix(pub, c): # 基底Mを生成
    N = len(pub)
    m_id = matrix.identity(N) * 2
    m = matrix(ZZ, 1, N + 1, pub[:] + [-c])
    B = m_id.augment(matrix(ZZ, N, 1, [-1] * N))
    m = m.stack(B)
    return m

def shortest_vector(matrix): # 最短経路（m[i][0]が0でそれ以外が-1, 1のベクトル）を検索
    for i in matrix.columns():
        if not(i[0]) and all([(j == -1 or j == 1) for j in i[1:]]):
            return i


d = len(pub_key) / log2(max(pub_key)) # 密度dを計算
print("d =", d)

M = create_matrix(pub_key, cipher) # 基底を張る
LLL_M = M.transpose().LLL().transpose() # LLLアルゴリズムで殴る
V = shortest_vector(LLL_M) # 最短経路を検索

# 最短経路のベクトルVは-1, 1で表されるので-1を0で置換し復号する
plane = "".join(list(map(str, V)))
plane = plane.replace("0", "")
plane = plane.replace("-1", "0")

print(long_to_bytes(int(plane, base=2)))
