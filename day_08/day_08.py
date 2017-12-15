#!/usr/bin/env python3


import re


def inc(regs, reg, num):
    regs[reg] = regs.get(reg, 0) + num


def dec(regs, reg,  num):
    regs[reg] = regs.get(reg, 0) - num


def oper(reg, num, op, regs):

    op(regs, reg, num)


def arrange_instruc(inst, id_patt, const_patt, oper_patt):
    ids = id_patt.findall(inst)
    consts = const_patt.findall(inst)
    opers = oper_patt.findall(inst)
    string = "oper('{}', {}, {}, regs) if regs.get('{}', 0) {} {} else regs.get('{}', 0)".format(
        ids[0],
        consts[0],
        ids[1],
        ids[3],
        opers[0],
        consts[1],

        ids[0])
    return string


def main():

    f = open('input.txt')

    regs = dict()
    id_patt = re.compile(r'[a-z]+')
    const_patt = re.compile(r'-?[0-9]+')
    oper_patt = re.compile(r'[<>=!]=?')

    for line in f:
        inst = arrange_instruc(line.strip(), id_patt, const_patt, oper_patt)
        eval(inst)

    print(max(regs.values()))


if __name__ == "__main__":
    main()
