#!/usr/bin/env python3
"""T36: verify every Boolean expression the BL chapter writes, by truth table.

The expressions below were transcribed by hand from the card text (papers/p3/cards/BL.md) and from the
QP / MS page renders (bars are lost in ms_text). Python operators: & AND, | OR, ~ NOT (on 0/1 via n()).
Run: ~/.venvs/alevel-cs/bin/python papers/p3/audit/truth_tables.py
"""
from itertools import product


def n(x):
    return 1 - x


def table(f, k):
    return [f(*v) & 1 for v in product((0, 1), repeat=k)]


CHECKS = []


def same(label, f, g, k):
    CHECKS.append((label, table(f, k) == table(g, k)))


def rows(label, f, k, ones):
    """f is 1 exactly on the listed input rows (strings like '0101')."""
    got = {''.join(map(str, v)) for v in product((0, 1), repeat=k) if f(*v) & 1}
    CHECKS.append((label, got == set(ones)))


# --- chapter law table (BL.md lines 37-46)
same('Identity', lambda a: a & 1, lambda a: a, 1)
same('Null AND', lambda a: a & 0, lambda a: 0, 1)
same('Null OR', lambda a: a | 1, lambda a: 1, 1)
same('Complement AND', lambda a: a & n(a), lambda a: 0, 1)
same('Complement OR', lambda a: a | n(a), lambda a: 1, 1)
same('Distributive OR form', lambda a, b, c: a | (b & c), lambda a, b, c: (a | b) & (a | c), 3)
same('Absorption AND', lambda a, b: a & (a | b), lambda a, b: a, 2)
same('Absorption OR', lambda a, b: a | (a & b), lambda a, b: a, 2)
same('Redundancy AND', lambda a, b: a & (n(a) | b), lambda a, b: a & b, 2)
same('Redundancy OR', lambda a, b: a | (n(a) & b), lambda a, b: a | b, 2)
same('De Morgan AND', lambda a, b: n(a & b), lambda a, b: n(a) | n(b), 2)
same('De Morgan OR', lambda a, b: n(a | b), lambda a, b: n(a) & n(b), 2)

# --- BL-01 9618_s24_31:6(a): circuit read from QP p.6; Z column must equal MS p.9
P = lambda a, b, c: n(b)
Z1 = lambda a, b, c: (a & b & c) | (a & P(a, b, c) & c) | (a ^ P(a, b, c))
rows('BL-01 s24/31 6(a) Z = MS p.9', Z1, 3, ['000', '001', '101', '110', '111'])
# 6(b) MS p.9 SOP: A'B'C' + A'B'C + AB'C + ABC' + ABC
same('BL-01/04 s24/31 6(b) SOP = circuit', Z1,
     lambda a, b, c: (n(a) & n(b) & n(c)) | (n(a) & n(b) & c) | (a & n(b) & c) | (a & b & n(c)) | (a & b & c), 3)

# --- BL-02 half adder / full adder (card lines 123-127; s21/31 MS p.8)
rows('BL-02 half adder sum', lambda a, b: a ^ b, 2, ['01', '10'])
rows('BL-02 half adder carry', lambda a, b: a & b, 2, ['11'])
same('BL-02 full adder sum SOP', lambda a, b, c: (n(a) & n(b) & c) | (n(a) & b & n(c)) | (a & n(b) & n(c)) | (a & b & c),
     lambda a, b, c: a ^ b ^ c, 3)
same('BL-02 full adder carry SOP', lambda a, b, c: (n(a) & b & c) | (a & n(b) & c) | (a & b & n(c)) | (a & b & c),
     lambda a, b, c: (a & b) | (a & c) | (b & c), 3)

# --- BL-04 / BL-06 / BL-07 9618_w24_31:7 (truth table QP p.6)
T_ROWS = ['0001', '0011', '1001', '1011', '1101', '1111']
SOP_T = lambda a, b, c, d: ((n(a) & n(b) & n(c) & d) | (n(a) & n(b) & c & d) | (a & n(b) & n(c) & d)
                            | (a & n(b) & c & d) | (a & b & n(c) & d) | (a & b & c & d))
rows('BL-04 w24/31 7(a) card SOP = QP table', SOP_T, 4, T_ROWS)
rows('BL-06 w24/31 7(d)(i) A.D + B\'.D = QP table', lambda a, b, c, d: (a & d) | (n(b) & d), 4, T_ROWS)
rows('BL-07 w24/31 7(d)(ii) D.(A + B\') (card, D41) = QP table', lambda a, b, c, d: d & (a | n(b)), 4, T_ROWS)
CHECKS.append(('BL-07 w24/31 7(d)(ii) MS-printed D.(A.B\') differs from table (expected False)',
               {''.join(map(str, v)) for v in product((0, 1), repeat=4) if (lambda a, b, c, d: d & a & n(b))(*v)} != set(T_ROWS)))

# --- BL-05 / BL-06 / BL-07 9618_s23_31:7 (expression QP p.8)
Z23 = lambda a, b, c, d: ((n(a) & n(b) & n(c) & n(d)) | (n(a) & n(b) & n(c) & d) | (n(a) & b & n(c) & n(d))
                          | (n(a) & b & n(c) & d) | (a & b & n(c) & n(d)) | (a & b & n(c) & d))
rows('BL-05 s23/31 7(a) K-map ones (card table)', Z23, 4, ['0000', '0001', '0100', '0101', '1100', '1101'])
same('BL-06 s23/31 7(c) A\'.C\' + B.C\'', Z23, lambda a, b, c, d: (n(a) & n(c)) | (b & n(c)), 4)
same('BL-07 s23/31 7(d) C\'.(A\' + B)', Z23, lambda a, b, c, d: n(c) & (n(a) | b), 4)

# --- BL-05 variation 9618_w24_32:6 (QP p.6): ones exactly on CD = 01 and CD = 10
rows('BL-05 w24/32 6 ones on CD=01/10', lambda a, b, c, d: c ^ d, 4,
     ['0001', '0010', '0101', '0110', '1001', '1010', '1101', '1110'])

# --- BL-06 variation 9618_w25_31:6(b) (MS p.11): A'.B + B.C' + A.B'.C
K3 = {'010', '011', '101', '110'}  # A,B,C rows from the MS K-map (A=0: BC 11,10; A=1: BC 01,10)
rows('BL-06 w25/31 6(b)(iii) MS answer = K-map', lambda a, b, c: (n(a) & b) | (b & n(c)) | (a & n(b) & c), 3, K3)

# --- BL-07 9618_w22_32:8(c) (QP p.7 bars): NOT[NOT(A'.B') . NOT(A'.C) . NOT(B.D)]
X = lambda a, b, c, d: n(n(n(a) & n(b)) & n(n(a) & c) & n(b & d))
same('BL-07 w22/32 8(c) -> A\'.B\' + A\'.C + B.D', X, lambda a, b, c, d: (n(a) & n(b)) | (n(a) & c) | (b & d), 4)
same('BL-07 w22/32 8(c) -> A\'.(B\' + C) + B.D', X, lambda a, b, c, d: (n(a) & (n(b) | c)) | (b & d), 4)

# --- BL-07 variation 9618_w23_31:6(b) (QP p.7): Y = A'B'C'D' + A'B'CD' + A'BC'D' + A'BCD'
Y = lambda a, b, c, d: ((n(a) & n(b) & n(c) & n(d)) | (n(a) & n(b) & c & n(d)) | (n(a) & b & n(c) & n(d))
                        | (n(a) & b & c & n(d)))
same('BL-07 w23/31 6(b) Y = A\'.D\'', Y, lambda a, b, c, d: n(a) & n(d), 4)

# --- BL-01 line 77: 9618_w23_32:7(a) three-input NOR
rows('BL-01 w23/32 7(a) 3-input NOR', lambda a, b, c: n(a | b | c), 3, ['000'])

# --- SR flip-flop (NOR) invalid state claim, card line 176: S = R = 1 -> Q = Q' = 0
nor = lambda x, y: n(x | y)
q, qb = 0, 1
for _ in range(4):
    q, qb = nor(1, qb), nor(1, q)  # R=1 into the Q gate, S=1 into the Q' gate
CHECKS.append(('BL-03 NOR SR S=R=1 gives Q=Q\'=0', (q, qb) == (0, 0)))

if __name__ == '__main__':
    bad = [c for c in CHECKS if not c[1]]
    for label, ok in CHECKS:
        print('ok  ' if ok else 'FAIL', label)
    print(f'{len(CHECKS) - len(bad)}/{len(CHECKS)} passed')
    raise SystemExit(1 if bad else 0)
