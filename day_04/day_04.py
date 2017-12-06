#!/usr/bin/env python


# part 1

def has_repeated(t):
    for i, elem1 in enumerate(t):
        if elem1 in t[i+1:]:
            return True
    return False


def count_valid_passphrase(phrases):
    return sum([1 for words in phrases if not has_repeated(words)])


def main():
    f = open('input.txt')
    count = count_valid_passphrase([line.strip().split() for line in f])
    print(count)


main()
