#!/usr/bin/env python


# part 1
def trampoline(t):
    current_pos = 0
    jump = 0
    count_steps = 0
    while current_pos < len(t):
        jump = t[current_pos]
        t[current_pos] = jump + 1
        current_pos = jump + current_pos
        count_steps += 1

    return count_steps


def trampoline2(t):
    current_pos = 0
    jump = 0
    count_steps = 0
    while current_pos < len(t):
        jump = t[current_pos]
        if jump >= 3:
            t[current_pos] = jump - 1
        else:
            t[current_pos] = jump + 1
        current_pos = jump + current_pos

        count_steps += 1

    return count_steps


def main():
    f = open('input.txt')

    t = [int(line.strip()) for line in f]

    # print(trampoline(t))

    print(trampoline2(t))
    # l1 = [0, 3, 0, 1, -3]
    # print(trampoline2(l1))

    # l1 = [0, 3, 0, 1, -3]

    # print('total', trampoline(l1))
    # l2 = [1, 3, 0, 1, -3]
    # l3 = [2, 3, 0, 1, -3]
    # l4 = [2, 4, 0, 1, -3]
    # l5 = [2, 4, 0, 1, -2]

    # 372671


if __name__ == "__main__":
    main()

