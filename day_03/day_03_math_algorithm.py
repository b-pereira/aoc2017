#!/usr/bin/env python
import math


def manhattan(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return abs(x2 - x1) + abs(y2 - y1)

# Resolution to find n-th number in a spiral matrix, based on the algorithm in
# https://math.stackexchange.com/a/163093 but with a twist =D!.  The accepted
# question is an algorithm to find the n-th number clockwise, but I altered the
# version to be counte-clockwise.

def spiral(n):

    k = 0
    tup = (0, 0)

    m = math.floor(math.sqrt(n))
    if m % 2 != 0:
        k = (m-1)//2
    elif m % 2 == 0 and n >= m*(m+1):
        k = m//2
    else:
        k = m//2 - 1
    n_step1 = (2*k + 0) * (2*k + 1)
    n_step2 = (2*k + 1) * (2*k + 1)
    n_step3 = (2*k + 2) * (2*k + 1)
    n_step4 = (2*k + 2) * (2*k + 2)
    n_step5 = (2*k + 2) * (2*k + 3)

    if n_step1 < n <= n_step2:
        tup = (n - 4 * (k**2) - 3*k, -k)
    elif n_step2 < n <= n_step3:
        tup = (k + 1, n - 4 * (k**2) - 5*k - 1)
    elif n_step3 < n <= n_step4:
        tup = (4 * (k**2) + 7*k + 3 - n, k + 1)
    elif n_step4 < n <= n_step5:
        tup = (-k - 1,  4 * (k**2) + 9*k + 5 - n)
    else:
        tup = (-k, -k)

    return tup


dicio = dict()
for i in range(1, 361527 + 1):
    dicio[i] = spiral(i - 1)


print(manhattan(dicio[361527], (0, 0)))
