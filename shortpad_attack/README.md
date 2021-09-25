# Coppersmith's short-pad attack

## 概要
2つの平文の差が十分に小さい場合、Coppersmith's short-pad attackで復号することができます。Frankin-Reiter Related Message Attackと違い、平文の差$d$が判明している必要はありません。

## 定理
以下の式（パディング処理）について考えます。

$$
m=\lfloor n/e^2 \rfloor \\
M_1=2^mM+r_1 \\
M_2=2^mM+r_2
$$

ここで、$M$は長さが最大$n-m$ bitのメッセージ、$r_1, r_2$は、$0≤r_1,r_2<2^m$を満たす整数です。

このとき、攻撃者が公開鍵の組$N, e$と$M_1, M_2$の暗号文$C_1, C_2$を得られれば、$M$を復号することができます。

## 攻撃
以下のような$g_1, g_2$を定義します。

$$
g_1(x, y)=x^e-C_1 \\
g_2(x, y)=(x+y)^e-C_2
$$

ここで、$y=r2-r1$のとき、多項式は$x=M_1$を共通根を持つことが分かります。つまり、$d=r_2-r_1$は終結式(resultant)$h(y)$の根となります。これで2変数の式を$y$だけの式にできたので、Coppersmith's Methodで解くことで$d$を求めることができます。
あとはFranklin-Reiter Related Message Attackで平文に復号することができます。

## 条件
終結式は展開すると$e^2$の多項式になるので、Coppersmith's Methodで方程式を解くことができるのは、
$$
|d|<2^m<N^{1/e^2} (∵2^{\lfloor n/e^2 \rfloor}<2^{n/e^2})
$$
となります。

$e=3, n=1024$の場合でも$|d|<2^{113}$なので、$e$が非常に小さい場合でのみでしか効果を発揮できない方法になります。

