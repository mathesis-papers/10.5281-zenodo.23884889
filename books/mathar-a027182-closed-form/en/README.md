# Why should a whole row obey a short rule?

Multiply a row of numbers by its reverse, entry by entry, and add the products. Can the answer be found without rebuilding the entire row each time? Haobo Ma and Wenlin Zhang answer this question for a number triangle introduced by Clark Kimberling. They give a closed formula for every row and use it to prove R. J. Mathar’s A027182 recurrence conjecture of 6 May 2026. The same binomial structure also yields recurrences for four related sequences.

Start with an example small enough to do by hand. Row two is $(5,10,5)$, giving

$$
5\cdot5+10\cdot10+5\cdot5=150.
$$

The answer is not $120$: the paper points out that arithmetic slip at the end of the OEIS example, while the OEIS term list agrees with $150$. The question is why a single formula works for rows of any length.

## From choosing objects to a row of numbers

The binomial coefficient $\binom Nk$ counts the ways to choose $k$ objects from $N$ distinct objects; for instance, $\binom42=6$. Row $N$ of Pascal’s triangle lists these numbers. Kimberling’s A027170 combines entries from neighboring Pascal rows. For integers $n\ge0$ and $0\le k\le n$, its original definition is

$$
\begin{aligned}
t(n,k)&=\binom{n+2}{k+1}+\binom{n+1}{k}\\
&\quad+\binom{n+1}{k+1}+\binom nk,\\
T(n,k)&=t(n,k)-t(0,0)+1\\
&=t(n,k)-4.
\end{aligned}
$$

Since $t(0,0)=5$, the correction of four matters. Pascal’s identity combines the two middle terms, giving the convenient form

$$
T(n,k)=2\binom{n+2}{k+1}+\binom nk-4.
$$

Here are the first few rows. Both row numbers and positions start at zero.

| $n$ | Row $n$ | Sum of squares |
|---|---|---|
| $0$ | $1$ | $1$ |
| $1$ | $3,3$ | $18$ |
| $2$ | $5,10,5$ | $150$ |
| $3$ | $7,19,19,7$ | $820$ |

Use $x$ to remember positions: set $g_n(x)=\sum_{k=0}^nT(n,k)x^k$. This polynomial simply packages a row; we need not assign a numerical value to $x$. For example, $g_2(x)=5+10x+5x^2$. The paper studies

$$
a_n=[x^n]g_n(x)^2,
$$

where $[x^n]$ means “take the coefficient of $x^n$.” In the product, two positions contribute exactly when they add to $n$, so

$$
a_n=\sum_{k=0}^nT(n,k)T(n,n-k).
$$

This is the self-convolution in this problem. Each row reads the same backward: $T(n,n-k)=T(n,k)$. Thus the convolution is a sum of squares. Symmetry removes the apparent difficulty of pairing different positions.

## The paper’s answer

A closed form computes the answer directly from $n$; a recurrence computes it from earlier answers. To keep the long recurrence readable, define the following expression, including its correction term. It is not a linear operator:

$$
\begin{aligned}
\mathcal R_n(f)={}&2(n+2)f_n\\
&-(17n+23)f_{n-1}\\
&+(47n+36)f_{n-2}\\
&-2(22n+17)f_{n-3}\\
&+4(20-n)f_{n-4}\\
&+8(2n-9)f_{n-5}\\
&+24(12n-47).
\end{aligned}
$$

::: {.theorem #main-formula title="Closed form and Mathar’s recurrence" mathesis="collected:mathar-a027182-closed-form:4:s1" status="written-proof" proof="pf-main-formula" doi="10.5281/zenodo.23884890" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/253"}
For every integer $n\ge0$,

$$
\begin{aligned}
a_n={}&4\binom{2n+4}{n+2}+4\binom{2n+2}{n+1}\\
&+\binom{2n}{n}-72\cdot2^n\\
&+16n+40.
\end{aligned}
$$

For every integer $n\ge6$, $\mathcal R_n(a)=0$.
:::

The complete written argument is in the [next chapter](proof.md). The original A027182 starts at $n=1$; the same construction supplies $a_0=1$. The closed form includes this boundary: $4\cdot6+4\cdot2+1-72+40=1$. With this extension the recurrence also holds at $n=5$; the public Lean theorem states the range $n\ge6$.

The gain is more than fewer multiplications. A whole row’s sum of squares becomes three neighboring central binomial coefficients $c_m=\binom{2m}{m}$, a power $2^n$, and an affine expression. Knowing how each part changes with the index explains why a fixed-length recurrence exists. It is an all-index argument, rather than a formula fitted to a finite list. The paper does not establish that the recurrence has minimal order.

## A map of the proof

Write a row entry as $2A_k+B_k-4$, with $A_k=\binom{n+2}{k+1}$ and $B_k=\binom nk$. Expanding the square leaves five kinds of sums besides the constant term. The binomial theorem evaluates all five. Next, the ratio of consecutive central binomial coefficients gives a second-order relation; suitable shifts then remove the exponential part. A shift must move the index-dependent coefficients as well as the sequence entries.

The film draws this same route, beginning with the pairings in row two and ending with the mechanism behind the closed form and recurrence.

::: {.film src="001-symmetry-to-recurrence"}
From a symmetric row to a recurrence: English narration and aligned Chinese/English subtitles explain the sum of squares and shifted cancellation.
:::

For a page-by-page mathematical talk, use the aligned Chinese and English academic presentation and its speaker notes.

::: {.slides src="seminar"}
Mathar’s conjecture: symmetry, closed form and recurrence.
:::

Continue with the [complete main proof](proof.md), then the [four companion recurrences](companions.md). [Evidence and contributions](sources.md) explains which statements have public Lean theorems and how to extend that correspondence.
