#!/usr/bin/env python


def part_01(seq):

    # current index position
    current_pos = 0
    # next index position
    # the list is circular. Thus, the mod operation is used to increment
    # the value of the index for both index positions
    next_pos = 1
    # accumulator for the sum
    acc = 0

    # iterate N times, knowing that N = number of elements
    for item in range(len(seq)):

        # the current list item is compared to the next
        # if they're equal the value of current element
        # is added
        if seq[current_pos] == seq[next_pos]:
            acc += seq[current_pos]

        # increment of the current and next position
        current_pos = (current_pos + 1) % len(seq)
        next_pos = (current_pos + 1) % len(seq)

    return acc


def part_02(seq):
    half = len(seq) // 2
    # current index position
    current_pos = 0
    next_pos = half
    # accumulator for the sum
    acc = 0

    # iterate N times, knowing that N = number of elements
    for item in range(len(seq)):

        # the current list item is compared to the next
        # if they're equal the value of current element
        # is added
        if seq[current_pos] == seq[next_pos]:
            acc += seq[current_pos]

        # increment of the current and next position
        current_pos = (current_pos + 1) % len(seq)
        next_pos = (current_pos + half) % len(seq)

    return acc


def main():
    f = open("input.txt")
    number_seq = [int(character) for character in f.readline().strip()]
    print(part_01(number_seq))
    print(part_02(number_seq))


if __name__ == "__main__":
    main()
    # print(part_02([1, 2, 1, 2]))
    # print(part_02([1, 2, 2, 1]))
    # print(part_02([1, 2, 3, 4, 2, 5]))
    # print(part_02([1, 2, 3, 1, 2, 3]))
    # print(part_02([1, 2, 1, 3, 1, 4, 1, 5]))
    # seq1 = [, 1, 1, 2, 2]
    # print(inverse_captcha(seq1))
    # seq2 = [1, 1, 1, 1]
    # print(inverse_captcha(seq2))
    # seq3 = [1, 2, 3, 4]
    # print(inverse_captcha(seq3))
    # seq4 = [9, 1, 2, 1, 2, 1, 2, 9]
    # print(inverse_captcha(seq4))
