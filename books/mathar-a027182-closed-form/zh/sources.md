# 证据、来源与贡献

本文解说的是 Haobo Ma 与 Wenlin Zhang 的论文第 4 版，原题为 *Proof of Mathar's conjecture on OEIS A027182: a closed form and the six-term recurrence*。精确版本 DOI 为 [10.5281/zenodo.23884890](https://doi.org/10.5281/zenodo.23884890)；[10.5281/zenodo.23884889](https://doi.org/10.5281/zenodo.23884889) 是整项作品的概念 DOI。原文与解说的许可均为 CC BY 4.0。Haobo Ma 的机构为 ChronoAI Pte Ltd, Singapore；Wenlin Zhang 的机构为 National University of Singapore 与 ChronoAI Pte Ltd, Singapore。

## 论证与形式证据的范围

[公开 Lean 源文件](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S1/Recurrence/MatharA027182SelfConvolution.lean)中的公开定理，按与原文一致的三角形及卷积定义，证明 A027182 在所有 $n\ge6$ 时的递推。源文件在论文记录的修订与本书所钉修订上相同。本书的[单列递推结论](proof.md#mathar-recurrence)准确引用它。源码中的私有闭式辅助证明并不使整个论文自动成为一条公开定理；完整闭式与三条伴随推论仍按原文的书面证明呈现。

论文另报告了截至 $n=400$ 的有限算术比较。这些计算可帮助发现错误，所有下标成立的结论依赖书面论证或其准确匹配的 Lean 定理；本解说没有重新执行随论文提供的程序。

| 待补齐的公开范围 | 共享贡献入口 |
|---|---|
| 主定理的全下标闭式；保留已有递推证明 | [A027182 闭式](https://github.com/the-omega-institute/trureturing-requests/issues/253) |
| A027171 与 A027175 的中间项递推 | [两种中间项](https://github.com/the-omega-institute/trureturing-requests/issues/254) |
| A027174 的近中间项递推 | [近中间项](https://github.com/the-omega-institute/trureturing-requests/issues/255) |
| A027179 的半行和递推 | [半行和](https://github.com/the-omega-institute/trureturing-requests/issues/256) |

这些是已在原文证明、待补齐上述公开形式化范围的结果。贡献者在对应请求下协调具体范围，在自己的 fork 中开聚焦分支，按[上游贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)向 trureturing 的 `dev` 提交 PR。合并后仍须核对公开声明与原文的定义、量词及边界，并更新本书的准确引用。GitHub 活动不等于平台核验收据或积分。

## 谁提出问题，谁提供公式？

Clark Kimberling 引入了 [A027170](https://oeis.org/A027170) 数三角形及 [A027182](https://oeis.org/A027182) 序列。论文所解的五条递推猜想由 R. J. Mathar 于 2026 年 5 月 6 日记录。Christian Krause 于 2026 年 5 月 10 日记录 [A027171](https://oeis.org/A027171) 闭式，于 5 月 11 日记录 [A027174](https://oeis.org/A027174) 与 [A027175](https://oeis.org/A027175) 闭式；本论文用这些公式证明相应递推，保留公式原有归属。[A027179](https://oeis.org/A027179) 的奇偶分解归于 Mathar。[A027178](https://oeis.org/A027178) 的行和公式由 Ralf Stephan 于 2004 年记录，OEIS 将 2026 年证明归于 Krause。这些日期及贡献归属按第 4 版原文所引的 OEIS 记录。

更一般的二项式和递推算法背景见 A. Bostan、P. Lairez 与 B. Salvy，*Multiple binomial sums*，Journal of Symbolic Computation **80** (2017), 351–386，[doi:10.1016/j.jsc.2016.04.002](https://doi.org/10.1016/j.jsc.2016.04.002)。这里的特色是直接利用行对称性求和，再用移位算子得到递推。
