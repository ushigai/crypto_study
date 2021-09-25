# Stereotyped message attack

## 概要
平文の一部が既知のとき、未知の部分に対してCopperSmith's Methodを適用することができます。

暗号文：$c$
既知部分：$B$

$$f(x)=(B+x_0)^e - c \mod  N$$

$f(x)$は展開すると、

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
B^{e-1}+B^e-c \mod N
$$

のようなモニック多項式になるので、$f(x_0)≡0 \mod N$と以下の条件を満たすような$x_0$を効率よく求めることができます。

$$|x_0| ≤ N^{1/e}$$


