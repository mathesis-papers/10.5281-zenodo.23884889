# Four companion recurrences: the same backbone

The main sequence uses a whole row’s sum of squares. Now take one middle entry, one near-middle entry, or the sum of the left half. These different-looking objects also reduce to central binomial coefficients and simple corrections. Keep $c_m=\binom{2m}m$ and $R_m=0$ from the previous chapter. These are Corollaries 2–4 of the manuscript; Corollary 2 treats two sequences.

## A middle entry

::: {.corollary #middle-entries title="Two middle-entry sequences" mathesis="collected:mathar-a027182-closed-form:4:s2" status="written-proof" proof="pf-middle-entries" doi="10.5281/zenodo.23884890" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/254"}

Let $u_n=T(2n,n)$ for $n\ge0$ (A027171), and $v_n=T(2n-1,n-1)$ for $n\ge1$ (A027175). The following holds for $f=u$ with $n\ge2$, and $f=v$ with $n\ge3$:


$$
\begin{aligned}
0={}&2(n+1)f_n-(7n+5)f_{n-1}\\
&+2(3-2n)f_{n-2}+12(1-3n).
\end{aligned}
$$


:::

::: {.proof #pf-middle-entries}
The closed forms recorded by Christian Krause on 10–11 May 2026 follow directly from the definition of $T$:


$$
\begin{aligned}
u_n&=d_n-4,\\
v_n&=\tfrac12d_n-4,\\
d_n&=2c_{n+1}+c_n=\frac{9n+5}{n+1}c_n.
\end{aligned}
$$


For $v$, use $\binom{2n+1}n=(2n+1)c_n/(n+1)$ and $\binom{2n-1}{n-1}=c_n/2$. Substituting $d$ into the three sequence terms gives


$$
\begin{aligned}
&2(n+1)d_n-(7n+5)d_{n-1}+2(3-2n)d_{n-2}\\
&\qquad=4R_n+4R_{n-1}+R_{n-2}=0.
\end{aligned}
$$


The three coefficients sum to $3-9n$. Subtracting $4$ contributes $36n-12$, canceled by $12(1-3n)$; replacing $d$ by $d/2$ preserves the zero homogeneous part. The lower bounds keep $u_{n-2}$ or $v_{n-2}$ in its original domain. For example, $u_0=1,u_1=10,u_2=42$ gives $252-190-2-60=0$ at $n=2$.
:::

## Two positions left of the middle

::: {.corollary #near-middle title="Near-middle recurrence" mathesis="collected:mathar-a027182-closed-form:4:s3" status="written-proof" proof="pf-near-middle" doi="10.5281/zenodo.23884890" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/255"}

Let $z_n=T(2n,n-2)$ for $n\ge2$ (A027174). For every integer $n\ge4$,


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
Krause’s closed form recorded on 11 May 2026 can be written as


$$
\begin{aligned}
z_n&=2\binom{2n+2}{n-1}+\binom{2n}{n-2}-4\\
&=r(n)c_n-4,\\
r(n)&=\frac{n(9n^2+14n+1)}{(n+1)(n+2)(n+3)}.
\end{aligned}
$$


The ratios of the two binomial coefficients to $c_n$ are $2n(2n+1)/((n+2)(n+3))$ and $n(n-1)/((n+1)(n+2))$, with the first multiplied by $2$. Call the coefficients of the three sequence terms $q_0,q_1,q_2$. Use


$$
\begin{aligned}
\frac{c_{n-1}}{c_n}&=\frac{n}{2(2n-1)},\\
\frac{c_{n-2}}{c_n}&=\frac{n(n-1)}{4(2n-1)(2n-3)}.
\end{aligned}
$$


Multiply $\sum_{j=0}^2q_j(n)r(n-j)c_{n-j}/c_n$ by $2(n+1)(n+2)(2n-1)$. It becomes the following polynomial, which can be checked by expansion:


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


All denominators used here are nonzero for $n\ge4$. Also $q_0+q_1+q_2=3(111n^2+456n+229)$, so the correction $-4$ supplies exactly the negative of the required inhomogeneous term.
:::

## Why does a half-row need a parity split?

An odd-numbered row has an even number of positions, so its halves pair perfectly. An even-numbered row has a middle position; including it in both halves counts it twice. In row $2$, the left half sums to $5+10=15$, while the full sum is $20$: indeed $(20+10)/2=15$. In row $3$, the left half is $7+19=26$, exactly half the full sum $52$.

::: {.corollary #half-row title="Seven-term half-row recurrence" mathesis="collected:mathar-a027182-closed-form:4:s4" status="written-proof" proof="pf-half-row" doi="10.5281/zenodo.23884890" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/256"}

Let $b_n=\sum_{k=0}^{\lfloor n/2\rfloor}T(n,k)$ for $n\ge0$ (A027179), and define


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


Then, for every integer $n\ge6$,


$$
\begin{aligned}
0={}&\sum_{j=0}^6p_j(n)b_{n-j}\\
&+4(-24n^2+196n-365).
\end{aligned}
$$


:::

::: {.proof #pf-half-row}
First use binomial row sums to obtain the full row:


$$
\begin{aligned}
S_n&=\sum_{k=0}^nT(n,k)\\
&=2(2^{n+2}-2)+2^n-4(n+1)\\
&=9\cdot2^n-4n-8.
\end{aligned}
$$


This is the A027178 row-sum formula recorded by Ralf Stephan in 2004, with proof credited to Krause in 2026. Using the parity decomposition recorded by Mathar, $b_n=S_n/2$ for odd $n$ and $b_n=(S_n+T(n,n/2))/2$ for even $n$. Define $w_{2m}=d_m=(9m+5)c_m/(m+1)$ and $w_{2m+1}=0$ for $m\ge0$. The even-row middle entry is $d_m-4$; the even-index indicator is $(1+(-1)^n)/2$. Thus


$$
\begin{aligned}
b_n={}&\frac92\,2^n-2n-5\\
&-(-1)^n+\frac12w_n\qquad(n\ge0).
\end{aligned}
$$


Put $(\mathcal Pf)_n=\sum_{j=0}^6p_j(n)f_{n-j}$. Expanding the seven coefficients above gives


$$
\begin{aligned}
\sum_{j=0}^6p_j(n)2^{-j}&=0,\\
\sum_{j=0}^6p_j(n)(-1)^j&=0,\\
\sum_{j=0}^6p_j(n)(-2(n-j)-5)&\\
\qquad=4(24n^2-196n+365)&.
\end{aligned}
$$


It remains to show $\mathcal Pw=0$. For even $n\ge6$ only $j=0,2,4,6$ remain; for odd $n\ge7$ only $j=1,3,5$ remain. Central binomial ratios give


$$
\begin{aligned}
\frac{(\mathcal Pw)_n}{c_{n/2}}&=\frac{E(n)}{8(n-3)(n-1)}&& (n\text{ even}),\\
\frac{(\mathcal Pw)_n}{c_{(n-1)/2}}&=\frac{O(n)}{4(n-2)}&& (n\text{ odd}).
\end{aligned}
$$


The two polynomial certificates are


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


Both zeros follow by expanding the displayed products. To specify how every term is obtained, let $\epsilon\in\{0,1\}$ be the parity of $n$. When $j\equiv\epsilon\pmod2$,


$$
\begin{aligned}
\frac{w_{n-j}}{c_{(n-\epsilon)/2}}={}&\frac{9(n-j)+10}{n-j+2}\\
&\cdot\prod_{\ell=0}^{(j-\epsilon)/2-1}
\frac{n-\epsilon-2\ell}{4(n-\epsilon-2\ell-1)}.
\end{aligned}
$$


An empty product is $1$; shifts of the other parity are zero. All denominators are nonzero in the stated ranges, and $n-j\ge0$. Thus $\mathcal Pw=0$. Apply $\mathcal P$ to the closed form for $b$: the exponential and alternating parts vanish, and the affine part leaves the polynomial that cancels the recurrence’s constant term. This completes the proof.
:::

These four recurrence proofs share the central binomial relation with the main recurrence, but that does not make them consequences of the public Lean theorem about the main sequence. Their [contribution links](sources.md) use the canonical shared-request route.
