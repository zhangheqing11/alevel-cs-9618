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

# ------------------------------------------------------------------ Dijkstra / A* (AI)


def graph(edges):
    g = {}
    for a, b, w in edges:
        g.setdefault(a, {})[b] = w
        g.setdefault(b, {})[a] = w
    return g


def dijkstra(g, s):
    dist, done, order = {n: float('inf') for n in g}, set(), []
    dist[s] = 0
    while len(done) < len(g):
        u = min((n for n in g if n not in done), key=lambda n: dist[n])
        done.add(u)
        order.append((u, dist[u]))
        for v, w in g[u].items():
            if v not in done and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist, order


# 9618_w23_32:8, edges read from QP p.7 (render); card AI.md lines 167-182, MS p.6 answers
G1 = graph([('S', 'A', 8), ('S', 'F', 10), ('A', 'B', 4), ('B', 'C', 8), ('B', 'D', 2), ('D', 'E', 2),
            ('C', 'E', 3), ('C', 'F', 9), ('E', 'F', 7)])
d, order = dijkstra(G1, 'S')
check('AI-03 w23/32 8 answers = MS p.6 (8,12,19,14,16,10)',
      [d[k] for k in 'ABCDEF'] == [8, 12, 19, 14, 16, 10])
check('AI-03 w23/32 8 visit order = card table (S,A,F,B,D,E,C)', [n for n, _ in order] == list('SAFBDEC'))
# 9618_w25_33:8, edges read from QP p.7 (render); MS p.12 answers
G2 = graph([('S', 'T', 6), ('S', 'Y', 22), ('T', 'V', 4), ('V', 'W', 3), ('V', 'X', 9), ('W', 'X', 5),
            ('X', 'Y', 3), ('X', 'Z', 10), ('Y', 'Z', 8)])
d, _ = dijkstra(G2, 'S')
check('AI-03 w25/33 8 answers = MS p.12 (6,10,13,18,21,28)', [d[k] for k in 'TVWXYZ'] == [6, 10, 13, 18, 21, 28])
check('AI-03 card line 192: Y via T,V,W,X = 21 < 22', 6 + 4 + 3 + 5 + 3 == 21 < 22)


def astar(g, h, s, t):
    """Textbook A*: expand the open node with the smallest f; ties broken by smaller h, then insertion order."""
    gs, parent, rows, closed = {s: 0}, {s: None}, [(s, s, 0)], set()
    cnt = itertools.count()
    heap = [(h[s], h[s], next(cnt), s)]
    while heap:
        f, _, _, u = heapq.heappop(heap)
        if u in closed:
            continue
        if u == t:
            break
        closed.add(u)
        for v, w in g[u].items():
            if v in closed:
                continue
            ng = gs[u] + w
            if ng < gs.get(v, float('inf')):
                gs[v], parent[v] = ng, u
                rows.append((u, v, ng))
                heapq.heappush(heap, (ng + h[v], h[v], next(cnt), v))
    path, n = [], t
    while n:
        path.append(n)
        n = parent[n]
    return gs[t], path[::-1], rows


# 9618_s23_32:10(b), graph and h read from QP p.12 (render); card AI.md lines 227-243, MS p.11
G3 = graph([('Begin', 'A', 5), ('Begin', 'B', 6), ('Begin', 'C', 5), ('Begin', 'D', 4), ('A', 'E', 6), ('A', 'End', 8),
            ('B', 'End', 7), ('C', 'G', 2), ('D', 'G', 6), ('E', 'F', 7), ('F', 'End', 1), ('F', 'G', 4), ('G', 'End', 7)])
H3 = dict(Begin=12, A=8, B=7, C=7, D=11, E=8, F=1, G=5, End=0)
cost, path, rows = astar(G3, H3, 'Begin', 'End')
check('AI-04 s23/32 10(b) path Begin-C-G-F-End cost 12', path == ['Begin', 'C', 'G', 'F', 'End'] and cost == 12)
card_rows = [('Begin', 'Begin', 0), ('Begin', 'A', 5), ('Begin', 'B', 6), ('Begin', 'C', 5), ('Begin', 'D', 4),
             ('C', 'G', 7), ('G', 'F', 11), ('G', 'End', 14), ('F', 'End', 12)]
check('AI-04 s23/32 10(b) table rows = card = MS p.11, except F->E', [r for r in rows if r[:2] != ('F', 'E')] == card_rows)
# the card's own step 4 (AI.md:208) would also write F -> E (g 18, f 26): E had no g yet; MS and card omit it
check('AI-04 s23/32 template step 4 also yields row F->E g=18 (finding: card does not explain the omission)',
      ('F', 'E', 18) in rows)
# 9618_w21_31:9(b) (variation), graph and h read from QP p.12 (render); MS p.9 final path
G4 = graph([('Home', 'A', 1), ('Home', 'B', 5), ('Home', 'C', 4), ('A', 'B', 3), ('A', 'E', 6), ('B', 'D', 2),
            ('B', 'School', 7), ('C', 'D', 6), ('D', 'School', 2), ('E', 'F', 1), ('E', 'School', 5), ('F', 'School', 3)])
H4 = dict(Home=14, A=10, B=7, C=9, D=6, E=3, F=3, School=0)
cost, path, rows = astar(G4, H4, 'Home', 'School')
check('AI-04 w21/31 9(b) path Home-A-E-F-School cost 11', path == ['Home', 'A', 'E', 'F', 'School'] and cost == 11)

if __name__ == '__main__':
    import sys
    extra = sys.argv[1:]
    bad = [c for c in CHECKS if not c[1]]
    for label, ok in CHECKS:
        print('ok  ' if ok else 'FAIL', label)
    print(f'{len(CHECKS) - len(bad)}/{len(CHECKS)} passed')
    raise SystemExit(1 if bad else 0)
