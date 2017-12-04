#!/usr/bin/env python
import math


def tup_sum(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def list_pow(t, times):
    return [item for item in t for i in range(times)]


def spiral(n):

    R = (1,  0)
    D = (0, -1)
    L = (-1, 0)
    U = (0,  1)
    pos = (0, 0)
    grads = []
    coords = []

    corner1 = [R, U]
    corner2 = [L, D]
    grads.extend(corner1)
    grads.extend(list_pow(corner2, 2))

    m = math.floor(math.sqrt(n))
    for i in range(1, m):
        if i % 2 != 0:
            grads.extend(list_pow(corner1, i + 2))
        if i % 2 == 0:
            grads.extend(list_pow(corner2, i + 2))
    i = 2
    for grad in grads:

        pos = tup_sum(pos, grad)
        coords.append(pos)
        if i > n:
            break

        i += 1

    return coords


ls = spiral(24)
i = 1
for x, y in ls:
    print(i, '(', x, ', ',  y, ')')
    i += 1


