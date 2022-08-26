from Crypto.Util.number import *
from random import randint

# pubkey:p,g,y
# seckey:x
p = getPrime(128)
g = primitive_root(p)
x = randint(0, p-2)
y = pow(g, x, p)

# encrypt
m = 123456789
r = randint(0, p-2)
c1 = pow(g, r, p)
c2 = m*pow(y, r, p) % p

print("c1 :", c1)
print("c2 :", c2)


# decrypt
d = pow(c1, p-1-x, p)
m = c2 * d % p
print("m :", m)


print(pow(g, r*x+p-1-x, p))
print(m * pow(g, r*x+p-1-x, p) % p)
