'use strict';
// Shared deterministic film engine; every scene is a pure function of its timeline.
function fade(S) { return clamp(S.u / 0.5) * clamp((S.d - S.u) / 0.5); }
function heading(en, zh, a) {
  txt(en, 960, 220, {size: 45, fam: F.disp, w: 700, align: 'center', c: C.white, a});
  txt(zh, 960, 272, {size: 30, fam: F.zh, align: 'center', c: C.dim, a});
}
function formula(s, y, a, size = 44, color = C.white) {
  txt(s, 960, y, {size, fam: F.math, align: 'center', c: color, a});
}
function numberRow(values, y, a, focus = -1) {
  values.forEach((v, k) => chip(660 + 300*k, y, 155, 86, String(v), k === focus ? C.now : C.cyan, a, 47, F.math));
}
SCENES.row = S => {
  const a = fade(S); badge(a, 'computed');
  heading('CAN A WHOLE ROW OBEY ONE RULE?', '一整行，能否听从一条规则？', a);
  numberRow([5,10,5], 390, a);
  const b = at(S,1,0.8)*a;
  numberRow([5,10,5], 560, b);
  [660,960,1260].forEach(x => arrow(x,443,x,504,C.cyan,b,3));
  formula('5 × 5  +  10 × 10  +  5 × 5  =  150', 735, b, 47);
  formula('ROW 2  ·  Kimberling’s A027170', 810, a, 26, C.dim);
};
SCENES.symmetry = S => {
  const a = fade(S); badge(a,'argued');
  heading('POSITIONS PAIR TO n', '位置之和为 n；对称配对变为平方', a);
  formula('g₂(x) = 5 + 10x + 5x²', 380, a, 54);
  numberRow(['x⁰','x¹','x²'], 500, a);
  const p = at(S,1,0.7)*a;
  // The two endpoints meet their reflected partners; the middle meets itself.
  arrow(660,548,1260,630,C.mag,p,3); arrow(1260,548,660,630,C.mag,p,3);
  arrow(960,548,960,630,C.cyan,p,3);
  formula('T(n, n−k) = T(n, k)', 695, p, 46);
  formula('aₙ = Σ T(n,k)T(n,n−k) = Σ T(n,k)²', 800, at(S,2,0.8)*a, 44);
};
SCENES.sums = S => {
  const a = fade(S); badge(a,'argued');
  heading('FIVE SUMS, ONE BINOMIAL IDENTITY', '五类和，来自同一个选择恒等式', a);
  formula('T(n,k) = 2Aₖ + Bₖ − 4', 360, a, 48);
  formula('Aₖ = C(n+2,k+1)     Bₖ = C(n,k)', 420, a, 32, C.dim);
  formula('Σ C(r,j)C(s,q−j) = C(r+s,q)', 510, at(S,2,0.6)*a, 46, C.cyan);
  const labels=['Σ Aₖ²','Σ AₖBₖ','Σ Bₖ²','Σ Aₖ','Σ Bₖ'];
  const vals=[68,20,6,14,4];
  labels.forEach((v,k) => {
    const x=340+310*k, p=at(S,1,0.7,k*0.13)*a;
    panel(x-135,570,270,180,p,C.cyan);
    txt(v,x,630,{size:34,fam:F.math,align:'center',a:p,c:C.white});
    txt(String(vals[k]),x,713,{size:47,fam:F.math,align:'center',a:at(S,3,0.6)*a,c:C.cyan});
  });
  formula('ROW 2:  A = (4,6,4),  B = (1,2,1)', 820, a, 28, C.dim);
};
SCENES.formula = S => {
  const a=fade(S); badge(a,'argued');
  heading('A CLOSED FORM FOR EVERY ROW', '每一行都成立的闭式', a);
  formula('cₘ = C(2m,m)     m = 0,1,2,…', 365, a, 42, C.cyan);
  const p=at(S,1,0.8)*a;
  panel(240,430,1440,270,p,C.argued);
  formula('aₙ = 4cₙ₊₂ + 4cₙ₊₁ + cₙ', 520, p, 62);
  formula('− 72·2ⁿ + 16n + 40', 625, p, 57);
  formula('n ≥ 0       a₀ = 1', 770, at(S,2,0.7)*a, 45);
  formula('Haobo Ma · Wenlin Zhang  |  Version 4', 832, a, 25, C.dim);
};
SCENES.shift = S => {
  const a=fade(S); badge(a,'argued');
  heading('SHIFT THE ENTIRE RELATION', '移位必须连同系数一起移动', a);
  formula('(m+1)cₘ₊₁ = 2(2m+1)cₘ', 355, a, 43, C.cyan);
  formula('hₘ = 4cₘ₊₂ + 4cₘ₊₁ + cₘ     Bh = 0', 420, at(S,1,0.6)*a, 35);
  const p=at(S,2,0.7)*a;
  chip(460,545,490,100,'(αm+β)2ᵐ',C.argued,p,39,F.math);
  arrow(720,545,830,545,C.cyan,p,3);
  chip(1060,545,390,100,'(E−2)²',C.cyan,p,43,F.math);
  arrow(1270,545,1380,545,C.cyan,p,3);
  chip(1480,545,120,100,'0',C.cyan,p,52,F.math);
  formula('E[2(m+4)fₘ₊₂] = 2(m+5)fₘ₊₃', 700, at(S,3,0.6)*a, 43);
  formula('L = (E−1)(E−2)² B', 780, p, 40);
  formula('La + known correction = 0    →    n ≥ 6', 835, at(S,3,0.6)*a, 29, C.dim);
};
SCENES.scope = S => {
  const a=fade(S);
  heading('ONE STRUCTURE, SEVERAL RECURRENCES', '同一个骨架，解释多条递推', a);
  panel(180,330,740,460,a,C.argued,'MANUSCRIPT PROOFS');
  txt('Closed form · all n ≥ 0',230,410,{size:35,fam:F.disp,c:C.white,a});
  txt('Middle + near-middle entries',230,490,{size:34,fam:F.disp,c:C.white,a});
  txt('Half rows: odd / even split',230,570,{size:34,fam:F.disp,c:C.white,a});
  txt('Mathar · Krause · Stephan',230,710,{size:29,fam:F.disp,c:C.dim,a:at(S,1,0.5)*a});
  const p=at(S,2,0.7)*a;
  panel(1000,330,740,460,p,C.lean,'PUBLIC LEAN THEOREM');
  txt('A027182 recurrence',1050,440,{size:44,fam:F.disp,c:C.white,a:p});
  txt('Every n ≥ 6',1050,530,{size:49,fam:F.math,c:C.lean,a:p});
  txt('Same row and convolution',1050,625,{size:31,fam:F.disp,c:C.white,a:p});
  txt('Six sequence terms + correction',1050,710,{size:29,fam:F.disp,c:C.dim,a:p});
  formula('Haobo Ma · Wenlin Zhang | doi:10.5281/zenodo.23884890', 846, a, 23, C.dim);
};
FILM.poster = () => {
  heading('FROM SYMMETRY TO A RECURRENCE', '从对称数行到递推式', 1);
  numberRow([5,10,5],410,1);
  formula('5² + 10² + 5² = 150',575,1,70,C.cyan);
  formula('symmetry  →  five sums  →  closed form  →  recurrence',700,1,33);
  formula('Haobo Ma · Wenlin Zhang  |  A027182',810,1,30,C.dim);
  formula('Version 4 · doi:10.5281/zenodo.23884890',862,1,24,C.dim);
};
