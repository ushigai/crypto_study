from pub_key import pub_key
from cipher import cipher
from math import log2

n = len(pub_key)
d = n / log2(max(pub_key))
print("d =", d)