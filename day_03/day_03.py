#!/usr/bin/env python
import math


def manhattan(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2 - x1) + abs(y2 - y1)


def spiral(n):

    root = math.sqrt(n)
    if root % 1 == 0 and root % 2 != 0:
        max_dim = math.floor(root)**2
    elif root % 2 != 0:
        max_dim = int((math.floor(root + math.floor(root) % 2 + 1))**2)

    pos = [(1, (0, 0))]

    i = 1

    for x in range(2, int(math.sqrt(max_dim) + 1)):
        if x % 2 != 0:
            pwer = x**2
            num = x-1
            south = (pwer, pwer - num*1)
            west = (pwer - num*1, pwer - num*2)
            north = (pwer - num*2, pwer - num*3)
            east = (pwer - num*3, pwer - (num*4 - 1))

            south_row_num = [x for x in range(south[1], south[0]+1)]
            west_row_num = [x for x in range(west[1], west[0]+1)]
            north_row_num = [x for x in range(north[1], north[0]+1)]
            east_row_num = [x for x in range(east[1], east[0]+1)]
            west_row_num.reverse()
            north_row_num.reverse()

            south_row_pos = [(x, -i) for x in range(-i, i+1)]
            west_row_pos = [(-i, y) for y in range(-i, i+1)]
            north_row_pos = [(x, i) for x in range(-i, i+1)]
            east_row_pos = [(i, y) for y in range(-i+1, i+1)]

            pos.extend(list(zip(south_row_num, south_row_pos)))
            pos.extend(list(zip(north_row_num, north_row_pos)))
            pos.extend(list(zip(east_row_num, east_row_pos)))
            pos.extend(list(zip(west_row_num, west_row_pos)))
            i += 1
    return dict(pos)


dic = spiral(361527)

print(dic[361527])
print(manhattan(dic[361527], (0, 0)))



