#!/usr/bin/env python


# part 1
# efficient
def has_repeated(t):
    for i, elem1 in enumerate(t):
        if elem1 in t[i+1:]:
            return True
    return False


# part 2
# not efficient but one-liner ;)
def has_anagrams(t):
    return sum(
        [(sorted(t[i]) == sorted(t[j]))
         for i in range(0, len(t)) for j in range(i+1, len(t))])


def count_valid_passphrase(phrases, f):
    return sum([1 for words in phrases if not f(words)])


def main():
    f = open('input.txt')
    phrases = [line.strip().split() for line in f]
    count_repeated = count_valid_passphrase(phrases, has_repeated)
    print(count_repeated)
    f.seek(0)
    count_anagrams = count_valid_passphrase(phrases, has_anagrams)
    print(count_anagrams)

if __name__ == "__main__":
    main()

# l1 = [["abcde", "fghij"],
#       ["abcde", "xyz", "ecdab"],
#       ["a", "ab", "abc", "abd", "abf", "abj"],
#       ["iiii", "oiii", "ooii", "oooi", "oooo"],
#       ["oiii", "ioii", "iioi", "iiio"]]
# print(count_valid_passphrase(l1, has_anagrams))
