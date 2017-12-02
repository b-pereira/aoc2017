#!/usr/bin/env python


def get_matrix(f):
    return [[int(num) for num in row] for row in [elem.split() for elem in f]]


def part_01(matrix):
    # for each row in the matrix we find the minimum and the maximum value of
    # the row. Then we subtract the values, and the result is stored in list,
    # and latter is summed
    checksum = sum([(max(row) - min(row)) for row in matrix])
    return checksum


def find_divisable(row):
    # to find the evenly divisible values (the pair where one divides another
    # with the result being an integer number), we traverse the row and for
    # each number we compare with all the different values from the row. Note
    # that there is only one pair, thence the return statement call as soon
    # they're founded
    for num1 in row:
        for num2 in row:
            if num1 != num2 and num1 % num2 == 0:
                return num2 // num2


def part_02(matrix):
    # For each row apply the function for finding the evenly divisible values,
    # and sum the result list
    checksum = sum([find_divisable(row) for row in matrix])
    return checksum


def main():
    f = open("input.txt")
    matrix = get_matrix(f)

    print(part_01(matrix))

#    print(find_divisable([5, 9, 2, 8]))
#    print(find_divisable([9, 4, 7, 3]))
#    print(find_divisable([3, 8, 6, 5]))

    print(part_02(matrix))


if __name__ == "__main__":
    main()

