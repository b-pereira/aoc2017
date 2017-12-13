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


# part 2
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

    print(trampoline(t))

    print(trampoline2(t))


if __name__ == "__main__":
    main()

