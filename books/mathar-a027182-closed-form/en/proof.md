# The main proof: evaluate first, then shift

This chapter gives the complete chain of reasoning for Theorem 1 of the manuscript. All sums are finite: no convergence or interchange of infinite sums is involved. We first obtain the closed form, then turn it into a recurrence.

::: {.proof #pf-main-formula}
**Step 1: symmetry removes the pairings.** Fix $n\ge0$ and put $A_k=\binom{n+2}{k+1}$ and $B_k=\binom nk$. Choosing a subset and choosing its complement give the same count, so $A_{n-k}=A_k$ and $B_{n-k}=B_k$. The convolution from the previous chapter becomes


$$
a_n=\sum_{k=0}^n(2A_k+B_k-4)^2.
$$


**Step 2: evaluate five sums.** Why should a sum of products become another binomial coefficient? Choose $q$ objects from two groups of sizes $r$ and $s$, and classify the choice by how many came from the first group:


$$
\sum_j\binom rj\binom s{q-j}=\binom{r+s}q.
$$


Out-of-range binomial coefficients are zero. Equivalently, compare coefficients of $x^q$ in $(1+x)^r(1+x)^s$. For $(r,s,q)=(n+2,n+2,n+2)$, our $A_k$ omits the two endpoints of the full row, each contributing $1$. For the mixed sum use $(n+2,n,n+1)$, set $j=k+1$, and use $\binom n{n-k}=\binom nk$; the omitted $j=0$ term is zero. For the squared $B_k$ sum use $(n,n,n)$. Finally, setting $x=1$ in a binomial expansion gives the ordinary row sums. Hence


$$
\begin{aligned}
\sum_{k=0}^n A_k^2&=\binom{2n+4}{n+2}-2,\\
\sum_{k=0}^n A_kB_k&=\binom{2n+2}{n+1},\\
\sum_{k=0}^n B_k^2&=\binom{2n}{n},\\
\sum_{k=0}^n A_k&=2^{n+2}-2,\qquad
\sum_{k=0}^n B_k=2^n.
\end{aligned}
$$


Expand the square, retaining every correction term:


$$
\begin{aligned}
a_n={}&4\sum A_k^2+4\sum A_kB_k+\sum B_k^2\\
&-16\sum A_k-8\sum B_k+16(n+1).
\end{aligned}
$$


After substitution, the exponential part is $-16\cdot2^{n+2}-8\cdot2^n=-72\cdot2^n$; the remaining correction is $-8+32+16(n+1)=16n+40$. This proves the closed form, including $n=0$.

**Step 3: find a second-order relation.** Put $c_m=\binom{2m}m$, $h_m=4c_{m+2}+4c_{m+1}+c_m$, and $p_m=16m+40$. Canceling factorials gives


$$
\begin{aligned}
R_m&:=(m+1)c_{m+1}-2(2m+1)c_m\\
&=0\qquad(m\ge0).
\end{aligned}
$$


Think of $B$ as the following operation on a sequence:


$$
\begin{aligned}
(Bf)_m={}&2(m+4)f_{m+2}\\
&-(7m+27)f_{m+1}-(4m+2)f_m.
\end{aligned}
$$


Substituting the definition of $h$ and grouping coefficients of $c_m,\ldots,c_{m+4}$ gives


$$
\begin{aligned}
(Bh)_m&=8R_{m+3}+12R_{m+2}\\
&\quad+6R_{m+1}+R_m=0.
\end{aligned}
$$


**Step 4: shift and cancel.** Let $(Ef)_m=f_{m+1}$. Applying $E-2$ twice kills both $m2^m$ and $2^m$. Define


$$
\begin{aligned}
Q(E)&=(E-1)(E-2)^2\\
&=E^3-5E^2+8E-4,\\
L&=Q(E)B.
\end{aligned}
$$


Here $E(Bf)_m=(Bf)_{m+1}$, so the coefficients must also change from $m$ to $m+1$. For example, the first term becomes $2(m+5)f_{m+3}$, rather than $2(m+4)f_{m+3}$. The full expansion is


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


Since $Bh=0$, we have $Lh=0$. Direct substitution in the other two parts gives


$$
\begin{aligned}
(B(2^{\bullet}))_m&=(-10m-24)2^m,\\
(Bp)_m&=-144m^2-744m-1016.
\end{aligned}
$$


The first is killed by $(E-2)^2$. For any quadratic $q_m=\alpha m^2+\beta m+\gamma$, expanding the shifts gives $(Q(E)q)_m=2\alpha m+\beta-3\alpha$. Therefore


$$
\begin{aligned}
L(2^{\bullet})&=0,\\
(Lp)_m&=-288m-312\\
&=-24(12m+13).
\end{aligned}
$$


The closed form is $a_m=h_m-72\cdot2^m+p_m$. By linearity of $L$, we obtain $(La)_m+24(12m+13)=0$ for every $m\ge0$. Put $m=n-5$: the six coefficients become those in the previous chapter, and the constant becomes $24(12n-47)$. This proves the recurrence for $n\ge6$ and also explains why it holds at $n=5$ after adjoining $a_0$.
:::

## Which part matches the public Lean theorem?

::: {.theorem #mathar-recurrence title="Mathar’s recurrence" mathesis="collected:mathar-a027182-closed-form:4:s1" lean="D5/S1/Recurrence/MatharA027182SelfConvolution.result"}
For the sequence $a_n=[x^n]g_n(x)^2$ defined in the first chapter, every natural number $n\ge6$ satisfies $\mathcal R_n(a)=0$.
:::

This isolates the recurrence conclusion of Theorem 1, rather than asserting a stronger main theorem. The public Lean statement uses the original definitions of $t,T,g,a$: in the natural numbers, $T$ first subtracts $t(0,0)$ and then adds $1$. On $0\le k\le n$, we have $\binom{n+2}{k+1}\ge2$ and $\binom nk\ge1$, hence $t(n,k)\ge5$ and the subtraction does not truncate. Recurrence coefficients and sequence values are cast to integers; $n\ge6$ also keeps $n-1,\ldots,n-5$ away from natural-number underflow. Thus the definitions, arithmetic domain and boundary match.

The public source contains a private proof of the closed form, but its public result statement asserts the recurrence for $n\ge6$. We therefore retain the full source theorem as an attributed written proof and cite the exactly matching recurrence separately. [Evidence and contributions](sources.md) links the source and the remaining scope.
