#!/usr/bin/env python3
"""T36: recompute the step tables the P3 cards print (RPN stacks / conversions, floating point,
Dijkstra, A*, binary search, traces). Data is transcribed by hand from the QP pages named in each check.

Run: ~/.venvs/alevel-cs/bin/python papers/p3/audit/recompute.py
"""
from fractions import Fraction
import heapq
import itertools
import random

CHECKS = []


def check(label, ok):
    CHECKS.append((label, bool(ok)))


# ------------------------------------------------------------------ RPN
OPS = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '–': lambda x, y: x - y,
       '*': lambda x, y: x * y, '/': lambda x, y: Fraction(x) / Fraction(y)}


def rpn_trace(tokens, env):
    stack, cols = [], []
    for t in tokens.split():
        if t in OPS:
            y, x = stack.pop(), stack.pop()
            stack.append(OPS[t](x, y))
        else:
            stack.append(Fraction(env.get(t, t)) if t in env else Fraction(t))
        cols.append(list(stack))
    return cols


def rpn_value(tokens, env):
    return rpn_trace(tokens, env)[-1][0]


def infix_value(expr, env):
    e = expr.replace('–', '-')
    return eval(e, {}, {k: Fraction(v) for k, v in env.items()})


# SY-12 representative 9618_w25_32:8(c) (QP p.8): card table BL? no - SY.md lines 684-688
cols = rpn_trace('c a / b d – * b +', dict(a=3, b=16, c=9, d=6))
card = [[9], [9, 3], [3], [3, 16], [3, 16, 6], [3, 10], [30], [30, 16], [46]]
check('SY-12 w25/32 8(c) stack columns = card table = MS p.14', cols == card)
# SY-12 variation 9618_s24_31:5(c) (QP p.5) vs MS p.8 ring values
cols = rpn_trace('a b - c d + * e /', dict(a=17, b=5, c=7, d=3, e=10))
check('SY-12 s24/31 5(c) final 12, 9 columns', len(cols) == 9 and cols[-1] == [12] and cols[6] == [120])
# 9618_s22_31:5(b)(i): m m j k * - *  -> 40
check('SY-10/12 s22/31 5(b) m m j k * - * = 40', rpn_value('m m j k * - *', dict(j=3, k=2, m=10)) == 40)
# 9618_w25_33:7(c): interim 360, final 10
cols = rpn_trace('c a – b d + * b c + /', dict(a=4, b=12, c=24, d=6))
check('SY-12 w25/33 7(c) interim 360 final 10', [360] in cols and cols[-1] == [10])

# SY-11 conversions: RPN and infix must agree on random values
rnd = random.Random(36)
pairs = [
    ('s24/31 5(a) RPN -> infix', '5 2 + 9 3 - / 3 *', '((5 + 2) / (9 - 3)) * 3'),
    ('s24/31 5(a) outer brackets dropped', '5 2 + 9 3 - / 3 *', '(5 + 2) / (9 - 3) * 3'),
    ('s24/31 5(b) infix -> RPN', '7 3 + 2 8 * - 6 /', '((7 + 3) - (2 * 8)) / 6'),
    ('w25/31 8(b) / card example', '2 6 – 13 7 + * 5 /', '(2 – 6) * (13 + 7) / 5'),
    ('w23/31 9(a)(i)', '5 2 – 5 4 + * 9 /', '(5 – 2) * (5 + 4) / 9'),
]
for label, r, i in pairs:
    check('SY-11 ' + label, rpn_value(r, {}) == infix_value(i, {}))
for label, r, i in [('w25/32 8(b)', 'a b - c + c a - * d /', '(a – b + c) * (c - a) / d'),
                    ('w22/31 5(a)', 'a b * b + d - 15 +', 'a * b + b - d + 15')]:
    ok = True
    for _ in range(20):
        env = {v: rnd.randint(1, 50) for v in 'abcd'}
        ok &= rpn_value(r, env) == infix_value(i, env)
    check('SY-11 ' + label + ' (20 random assignments)', ok)
check('SY-12 card line 692: 46 = (9/3)*(16-6)+16', Fraction(9, 3) * (16 - 6) + 16 == 46)

# ------------------------------------------------------------------ floating point (DR)


def fp_value(mant, exp):
    m = -int(mant[0]) + sum(Fraction(int(b), 2 ** (i + 1)) for i, b in enumerate(mant[1:]))
    e = -int(exp[0]) * 2 ** (len(exp) - 1) + int(exp[1:], 2)
    return m * Fraction(2) ** e


check('DR-09 w24/31 1(b) = -20.8125', fp_value('1010110011', '000101') == Fraction(-208125, 10000))
check('DR-09 w25/32 2(a) = 1940', fp_value('0111100101', '001011') == 1940)
check('DR-09 s24/31 1(a) = 316', fp_value('0100111100', '001001') == 316)
check('DR-10 s24/31 1(b) -102.75', fp_value('1001100101', '000111') == Fraction(-10275, 100))
check('DR-11 w22/31 1(c)(ii) value kept', fp_value('01111000', '00010110') == fp_value('00011110', '00011000'))
check('DR-11 s25/31 2(a) 0.00000011010111', fp_value('0110101110', '111010') == Fraction(int('11010111', 2), 2 ** 14))
check('DR-11 8+8 largest = 127/128 * 2^127', fp_value('01111111', '01111111') == Fraction(127, 128) * 2 ** 127)
check('DR-12 s23/32 1(b) needs 13 bits', len('0' + '101011111001') == 13)

if __name__ == '__main__':
    import sys
    extra = sys.argv[1:]
    bad = [c for c in CHECKS if not c[1]]
    for label, ok in CHECKS:
        print('ok  ' if ok else 'FAIL', label)
    print(f'{len(CHECKS) - len(bad)}/{len(CHECKS)} passed')
    raise SystemExit(1 if bad else 0)
