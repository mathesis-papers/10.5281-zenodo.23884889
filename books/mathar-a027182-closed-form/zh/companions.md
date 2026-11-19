# 四条伴随递推：同一个骨架

主序列用了整行的平方和。现在只取中间的一个数、靠近中间的一个数，或左半行的和。它们看似不同，却都能拆成中心二项式数及简单修正。这里沿用 $c_m=\binom{2m}m$ 和上一章的 $R_m=0$。以下是原文的 Corollaries 2–4；Corollary 2 同时处理两条序列。

## 中间的一项

::: {.corollary #middle-entries title="两种中间项" mathesis="collected:mathar-a027182-closed-form:4:s2" status="written-proof" proof="pf-middle-entries" doi="10.5281/zenodo.23884890" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/254"}

令 $u_n=T(2n,n)$，$n\ge0$（A027171）；令 $v_n=T(2n-1,n-1)$，$n\ge1$（A027175）。下式对 $f=u$、$n\ge2$ 及 $f=v$、$n\ge3$ 成立：


$$
\begin{aligned}
0={}&2(n+1)f_n-(7n+5)f_{n-1}\\
&+2(3-2n)f_{n-2}+12(1-3n).
\end{aligned}
$$


:::

::: {.proof #pf-middle-entries}
Christian Krause 在 2026 年 5 月 10–11 日记录的闭式由 $T$ 的定义直接得到：


$$
\begin{aligned}
u_n&=d_n-4,\\
v_n&=\tfrac12d_n-4,\\
d_n&=2c_{n+1}+c_n=\frac{9n+5}{n+1}c_n.
\end{aligned}
$$


对 $v$，用 $\binom{2n+1}n=(2n+1)c_n/(n+1)$ 及 $\binom{2n-1}{n-1}=c_n/2$ 即可。将 $d$ 代入递推的三个含序列项，得到


$$
\begin{aligned}
&2(n+1)d_n-(7n+5)d_{n-1}+2(3-2n)d_{n-2}\\
&\qquad=4R_n+4R_{n-1}+R_{n-2}=0.
\end{aligned}
$$


三个系数之和为 $3-9n$，所以减去 $4$ 带来 $36n-12$，恰被 $12(1-3n)$ 抵消；把 $d$ 换成 $d/2$ 仍然成立。下界保证 $u_{n-2}$ 或 $v_{n-2}$ 在原定义域内。例如 $u_0=1,u_1=10,u_2=42$，在 $n=2$ 时是 $252-190-2-60=0$。
:::

## 离中间两格

::: {.corollary #near-middle title="近中间项的递推" mathesis="collected:mathar-a027182-closed-form:4:s3" status="written-proof" proof="pf-near-middle" doi="10.5281/zenodo.23884890" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/255"}

令 $z_n=T(2n,n-2)$，$n\ge2$（A027174）。对每个整数 $n\ge4$，


$$
\begin{aligned}
0={}&-2(n+3)(139n-175)z_n\\
&+(1279n^2+1334n-1089)z_{n-1}\\
&-2(167n+121)(2n-3)z_{n-2}\\
&+12(111n^2+456n+229).
\end{aligned}
$$


:::

::: {.proof #pf-near-middle}
Krause 于 2026 年 5 月 11 日记录的闭式可写成


$$
\begin{aligned}
z_n&=2\binom{2n+2}{n-1}+\binom{2n}{n-2}-4\\
&=r(n)c_n-4,\\
r(n)&=\frac{n(9n^2+14n+1)}{(n+1)(n+2)(n+3)}.
\end{aligned}
$$


两个二项式数除以 $c_n$ 的比值分别为 $2n(2n+1)/((n+2)(n+3))$ 与 $n(n-1)/((n+1)(n+2))$，第一项还要乘以 $2$。记递推里三个序列项的系数为 $q_0,q_1,q_2$。再用


$$
\begin{aligned}
\frac{c_{n-1}}{c_n}&=\frac{n}{2(2n-1)},\\
\frac{c_{n-2}}{c_n}&=\frac{n(n-1)}{4(2n-1)(2n-3)}.
\end{aligned}
$$


把 $\sum_{j=0}^2q_j(n)r(n-j)c_{n-j}/c_n$ 乘以 $2(n+1)(n+2)(2n-1)$，得到下列可直接展开核对的多项式：


$$
\begin{aligned}
0={}&-4n(2n-1)(139n-175)\\
&\qquad\cdot(9n^2+14n+1)\\
&+(n-1)(9n^2-4n-4)\\
&\qquad\cdot(1279n^2+1334n-1089)\\
&-(n-2)(n+2)(167n+121)\\
&\qquad\cdot(9n^2-22n+9).
\end{aligned}
$$


在 $n\ge4$ 时所用分母全不为零。又有 $q_0+q_1+q_2=3(111n^2+456n+229)$，因此 $-4$ 的修正恰好给出所需非齐次项的负值。
:::

## 半行为什么必须分奇偶？

奇数行有偶数个位置，左右两半完全配对；偶数行有一个中间位置，左右两半若都包含它，就会多算一次。例如第 $2$ 行左半和是 $5+10=15$，而全行和是 $20$；$(20+10)/2=15$。第 $3$ 行左半和是 $7+19=26$，恰是全行和 $52$ 的一半。

::: {.corollary #half-row title="半行和的七项递推" mathesis="collected:mathar-a027182-closed-form:4:s4" status="written-proof" proof="pf-half-row" doi="10.5281/zenodo.23884890" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/256"}

令 $b_n=\sum_{k=0}^{\lfloor n/2\rfloor}T(n,k)$，$n\ge0$（A027179），并定义


$$
\begin{aligned}
p_0(n)&=-(n+2)(3n-20),\\
p_1(n)&=-(n+1)(3n-11),\\
p_2(n)&=33n^2-180n-100,\\
p_3(n)&=15n^2-56n+1,\\
p_4(n)&=2(-51n^2+313n-208),\\
p_5(n)&=-12(n-1)(n-4),\\
p_6(n)&=8(9n-11)(n-5).
\end{aligned}
$$


则对每个整数 $n\ge6$，


$$
\begin{aligned}
0={}&\sum_{j=0}^6p_j(n)b_{n-j}\\
&+4(-24n^2+196n-365).
\end{aligned}
$$


:::

::: {.proof #pf-half-row}
先用二项式行和计算整行：


$$
\begin{aligned}
S_n&=\sum_{k=0}^nT(n,k)\\
&=2(2^{n+2}-2)+2^n-4(n+1)\\
&=9\cdot2^n-4n-8.
\end{aligned}
$$


这是 Ralf Stephan 于 2004 年记录、Krause 于 2026 年获署名证明的 A027178 行和公式。按照 Mathar 记录的奇偶分解，奇数 $n$ 时 $b_n=S_n/2$，偶数 $n$ 时 $b_n=(S_n+T(n,n/2))/2$。定义 $w_{2m}=d_m=(9m+5)c_m/(m+1)$、$w_{2m+1}=0$，$m\ge0$。偶数行中间项是 $d_m-4$；偶数指示函数是 $(1+(-1)^n)/2$。故


$$
\begin{aligned}
b_n={}&\frac92\,2^n-2n-5\\
&-(-1)^n+\frac12w_n\qquad(n\ge0).
\end{aligned}
$$


令 $(\mathcal Pf)_n=\sum_{j=0}^6p_j(n)f_{n-j}$。展开上面七个系数得到


$$
\begin{aligned}
\sum_{j=0}^6p_j(n)2^{-j}&=0,\\
\sum_{j=0}^6p_j(n)(-1)^j&=0,\\
\sum_{j=0}^6p_j(n)(-2(n-j)-5)&\\
\qquad=4(24n^2-196n+365)&.
\end{aligned}
$$


剩下只需证 $\mathcal Pw=0$。偶数 $n\ge6$ 只保留 $j=0,2,4,6$，奇数 $n\ge7$ 只保留 $j=1,3,5$。中心二项式比值给出


$$
\begin{aligned}
\frac{(\mathcal Pw)_n}{c_{n/2}}&=\frac{E(n)}{8(n-3)(n-1)}&& (n\text{ even}),\\
\frac{(\mathcal Pw)_n}{c_{(n-1)/2}}&=\frac{O(n)}{4(n-2)}&& (n\text{ odd}).
\end{aligned}
$$


这里的两个多项式证书是


$$
\begin{aligned}
E(n)={}&-8(n-3)(n-1)\\
&\qquad\cdot(3n-20)(9n+10)\\
&+2(n-3)(9n-8)\\
&\qquad\cdot(33n^2-180n-100)\\
&-n(9n-26)\\
&\qquad\cdot(51n^2-313n+208)\\
&+n(n-2)(9n-44)(9n-11)\\
&=0,\\
O(n)={}&-4(n-2)(3n-11)(9n+1)\\
&+(9n-17)(15n^2-56n+1)\\
&-3(n-1)^2(9n-35)=0.
\end{aligned}
$$


两式的零值可直接展开检查。为把每项如何得到也写清楚，令 $\epsilon\in\{0,1\}$ 是 $n$ 的奇偶性；当 $j\equiv\epsilon\pmod2$ 时，


$$
\begin{aligned}
\frac{w_{n-j}}{c_{(n-\epsilon)/2}}={}&\frac{9(n-j)+10}{n-j+2}\\
&\cdot\prod_{\ell=0}^{(j-\epsilon)/2-1}
\frac{n-\epsilon-2\ell}{4(n-\epsilon-2\ell-1)}.
\end{aligned}
$$


空乘积为 $1$，另一种奇偶性的移位为零。所述范围内所有分母均非零，且 $n-j\ge0$。因此 $\mathcal Pw=0$。把 $\mathcal P$ 作用在 $b$ 的闭式上，指数项与交替项消失，一次式留下恰好抵消递推常数项的多项式，证明完成。
:::

这四条递推的书面证明与主递推共用中心二项式关系，但并不因此自动被主序列的 Lean 定理覆盖。各自的[贡献入口](sources.md)指向同一套共享请求流程。
