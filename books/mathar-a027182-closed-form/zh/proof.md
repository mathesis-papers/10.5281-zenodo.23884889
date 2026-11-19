# 完整主证明：先求和，再移位

本章给出原文 Theorem 1 的完整推理链。所有和都是有限和；没有收敛或交换无穷求和的步骤。先解释闭式，再把它变成递推。

::: {.proof #pf-main-formula}
**第一步：用对称性消去配对。** 固定 $n\ge0$，令 $A_k=\binom{n+2}{k+1}$、$B_k=\binom nk$。选择一个集合与选择其补集的方法数相同，因此 $A_{n-k}=A_k$、$B_{n-k}=B_k$。上一章的卷积遂变成


$$
a_n=\sum_{k=0}^n(2A_k+B_k-4)^2.
$$


**第二步：计算五类和。** 为什么乘积的和又是一个二项式数？从两组分别有 $r$ 与 $s$ 个对象的集合里选出 $q$ 个，按第一组选了多少个来分类，就有


$$
\sum_j\binom rj\binom s{q-j}=\binom{r+s}q.
$$


超出范围的二项式数按零处理。这也正是展开 $(1+x)^r(1+x)^s$ 后比较 $x^q$ 系数得到的恒等式。取 $(r,s,q)=(n+2,n+2,n+2)$ 时，我们的 $A_k$ 漏掉完整行的两个端点，各贡献 $1$。混合和取 $(n+2,n,n+1)$：令 $j=k+1$ 并使用 $\binom n{n-k}=\binom nk$；漏掉的 $j=0$ 项是零。平方 $B_k$ 的和取 $(n,n,n)$。最后，把二项式展开中的 $x$ 取为 $1$，得到普通的行和。因此


$$
\begin{aligned}
\sum_{k=0}^n A_k^2&=\binom{2n+4}{n+2}-2,\\
\sum_{k=0}^n A_kB_k&=\binom{2n+2}{n+1},\\
\sum_{k=0}^n B_k^2&=\binom{2n}{n},\\
\sum_{k=0}^n A_k&=2^{n+2}-2,\qquad
\sum_{k=0}^n B_k=2^n.
\end{aligned}
$$


展开平方，每个修正项都要保留：


$$
\begin{aligned}
a_n={}&4\sum A_k^2+4\sum A_kB_k+\sum B_k^2\\
&-16\sum A_k-8\sum B_k+16(n+1).
\end{aligned}
$$


代入后，指数项为 $-16\cdot2^{n+2}-8\cdot2^n=-72\cdot2^n$；其余修正是 $-8+32+16(n+1)=16n+40$。这就证明了闭式，包括 $n=0$。

**第三步：找到二阶关系。** 令 $c_m=\binom{2m}m$、$h_m=4c_{m+2}+4c_{m+1}+c_m$、$p_m=16m+40$。阶乘约分给出


$$
\begin{aligned}
R_m&:=(m+1)c_{m+1}-2(2m+1)c_m\\
&=0\qquad(m\ge0).
\end{aligned}
$$


把下面的 $B$ 看作对序列做的一套运算：


$$
\begin{aligned}
(Bf)_m={}&2(m+4)f_{m+2}\\
&-(7m+27)f_{m+1}-(4m+2)f_m.
\end{aligned}
$$


将 $h$ 的定义代入，两边按 $c_m,\ldots,c_{m+4}$ 分组，得到


$$
\begin{aligned}
(Bh)_m&=8R_{m+3}+12R_{m+2}\\
&\quad+6R_{m+1}+R_m=0.
\end{aligned}
$$


**第四步：移位并消去。** 令 $(Ef)_m=f_{m+1}$。对 $m2^m$ 与 $2^m$，连续做两次 $E-2$ 就得到零。定义


$$
\begin{aligned}
Q(E)&=(E-1)(E-2)^2\\
&=E^3-5E^2+8E-4,\\
L&=Q(E)B.
\end{aligned}
$$


这里 $E(Bf)_m=(Bf)_{m+1}$，所以系数也必须从 $m$ 换成 $m+1$。例如第一项成为 $2(m+5)f_{m+3}$，不是 $2(m+4)f_{m+3}$。完整展开为


$$
\begin{aligned}
(Lf)_m={}&2(m+7)f_{m+5}\\
&-(17m+108)f_{m+4}\\
&+(47m+271)f_{m+3}\\
&-(44m+254)f_{m+2}\\
&+(60-4m)f_{m+1}\\
&+(16m+8)f_m.
\end{aligned}
$$


由于 $Bh=0$，有 $Lh=0$。直接代入另外两部分，


$$
\begin{aligned}
(B(2^{\bullet}))_m&=(-10m-24)2^m,\\
(Bp)_m&=-144m^2-744m-1016.
\end{aligned}
$$


前一式被 $(E-2)^2$ 消去。对任意二次式 $q_m=\alpha m^2+\beta m+\gamma$，逐项展开有 $(Q(E)q)_m=2\alpha m+\beta-3\alpha$。于是


$$
\begin{aligned}
L(2^{\bullet})&=0,\\
(Lp)_m&=-288m-312\\
&=-24(12m+13).
\end{aligned}
$$


闭式写成 $a_m=h_m-72\cdot2^m+p_m$。由 $L$ 的线性性，$(La)_m+24(12m+13)=0$ 对一切 $m\ge0$ 成立。取 $m=n-5$，上述六个系数依次变为上一章的系数，常数项成为 $24(12n-47)$。这证明了 $n\ge6$ 的递推，也说明补入 $a_0$ 后为何 $n=5$ 仍成立。
:::

## 公开 Lean 定理准确对应哪一部分？

::: {.theorem #mathar-recurrence title="Mathar 递推式" mathesis="collected:mathar-a027182-closed-form:4:s1" lean="D5/S1/Recurrence/MatharA027182SelfConvolution.result"}
对第一章定义的序列 $a_n=[x^n]g_n(x)^2$，每个自然数 $n\ge6$ 都满足 $\mathcal R_n(a)=0$。
:::

这单列的是原文 Theorem 1 的递推结论，不是另一条更强的主定理。公开 Lean 声明的 $t,T,g,a$ 使用原始定义：$T$ 在自然数中先减去 $t(0,0)$，再加 $1$。在 $0\le k\le n$ 时，$\binom{n+2}{k+1}\ge2$ 且 $\binom nk\ge1$，故 $t(n,k)\ge5$，自然数减法不会截断。所有递推系数与序列值先转为整数；$n\ge6$ 也保证 $n-1,\ldots,n-5$ 不涉及自然数下溢。这就对齐了定义、算术域与边界。

公开源码包含用于闭式的私有证明，但公开的结果声明只陈述 $n\ge6$ 的递推。因而本书把完整主定理保留为带出处的书面证明，把这个准确匹配的递推单独引用。[证据与贡献](sources.md)给出源码及待补齐的范围。
