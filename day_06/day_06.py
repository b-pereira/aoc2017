#!/usr/bin/env python


# # # # #
# Part 1
#
def distribute(t, max_block, max_block_index):

    # set next position for next block. Note that the list is circular
    i = (max_block_index + 1) % len(t)

    # previous block is reseted
    t[max_block_index] = 0

    # while whole block isn't redistribuidd
    while max_block > 0:

        # add one block
        t[i] = t[i] + 1

        # remove 1 block from the total block value to redistribute
        max_block -= 1

        # list is circular
        i = (i + 1) % len(t)

    return t


def mem_realloc(t):

    # there aren't any configurations
    dicio = dict()

    # there aren't any cycles yet
    cycle = 0

    # while configuration hasn't been seen before
    while dicio.get(tuple(t), 0) < 2:

        # get the max value to redistribute
        max_block = max(t)

        # get index for the max value. Note that if repeated the return value
        # is lowest index
        max_block_index = t.index(max_block)

        # redistribute block
        t = distribute(t, max_block, max_block_index)

        # save configuration
        dicio[tuple(t)] = dicio.get(tuple(t), 0) + 1

        # number of cycles is incremented
        cycle += 1

    return cycle


def main():

    f = open('input.txt')

    ls = [int(value) for value in f.readline().replace("\t\n", "").split()]

    print(mem_realloc(ls))


if __name__ == "__main__":
    main()
