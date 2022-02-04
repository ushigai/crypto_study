# Stereotyped message attack

## 概要
平文の一部が既知のとき、未知の部分に対してCopperSmith's Methodを適用することができます。

## 攻撃

暗号文と既知部分をそれぞれ$C, B$とすると、

$$
f(x)=(B+x_0)^e - C \mod N
$$

で、$f(x)$は展開すると、

$$
f(x)=x^e + 
\begin{pmatrix} 
e \\
1
\end{pmatrix}
Bx^{e-1}+ \dots +
\begin{pmatrix} 
e \\
e-1
\end{pmatrix}
B^{e-1}+B^e-C \mod N
$$

のようなモニック多項式になるので、$f(x_0)≡0 \mod N$を満たすような$x_0$を効率よく求めることができます。

## 条件
展開したとき$e$のモニック多項式になるので、
$$
|x_0| ≤ N^{1/e}
$$
という条件のもとで成り立つ攻撃となります。

