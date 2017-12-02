#!/usr/bin/env python


def main():
    f = open("input.txt")
    num_l = [[int(num) for num in row] for row in [elem.split() for elem in f]]
    checksum = sum([(max(row) - min(row)) for row in num_l])
    print(checksum)


if __name__ == "__main__":
    main()

