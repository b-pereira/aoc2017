#!/usr/bin/env python


def dxdy_generator(direction):
    if direction == 'ne':
        return (1, 1)
    elif direction == 'se':
        return (1, -1)
    elif direction == 'nw':
        return (-1, 1)
    elif direction == 'sw':
        return (-1, -1)
    elif direction == 's':
        return (0, -2)
    elif direction == 'n':
        return (0, 2)


def hex_distance(x, y):
    abs_x, abs_y = abs(x), abs(y)
    res = (abs_x + abs_y)//2
    return res


def main():

    _input = [line.strip().split(',') for line in open('input.txt')][0]
    dxdy = [dxdy_generator(elem) for elem in _input]

    x, y = (0, 0)
    res = 0

    for deriv in dxdy:
        dx, dy = deriv
        x, y = x + dx, y + dy
        if hex_distance(x, y) > res:
            res = hex_distance(x, y)

    print(x, y)

    print(hex_distance(x, y))

    print(res)


if __name__ == "__main__":
    main()
