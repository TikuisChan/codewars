from fractions import Fraction
from math import ceil

def decompose(n):
    n = Fraction(n)
    a, b = n.numerator, n.denominator
    if b == 1 and a >= 1:
        return [str(a)]
    else:
        ans = []
    while a > 0:
        deno = ceil(b/a)
        if deno == 1:
            ans.append('1')
        else:
            ans.append('1/' + str(deno))
        a = (- b) % a
        b = b * deno
    return ans
