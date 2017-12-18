#!/usr/bin/env python


import re


def score(lst):
    group = 0
    acc = 0
    for elem in lst:
        if elem == '{':
            group += 1
        elif elem == '}':
            acc += group
            group -= 1

    return acc


def main():

    _input = open('input.txt')

    lines = []
    total = 0
    total_garbage = 0
    cnl = re.compile(r'!.')
    grb = re.compile(r'<[^>]*>')
    grp = re.compile(r'{|}')

    # # part 1
    # for line in _input:

    #     line = grp.findall(grb.sub("", cnl.sub("", line.strip())))
    #     total += score(line)

    # print(total)


    # #_input.seek(0)

    for line in _input:
        lines.extend(grb.findall(cnl.sub("", line.strip())))

    for elem in lines:
        total_garbage += len(elem[1:len(elem)-1])

    print(total_garbage)



if __name__ == "__main__":
    main()
