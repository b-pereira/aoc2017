#!/usr/bin/env python


# if tree node is a leaf
def is_leaf(node):
    return len(node) == 0


# I'm using dictionaries with the key type str and value type list and creating
# dictionary key type str and value type dict. Thence, a node of the tree that
# is visited is a dictionary or a list otherwise. I'm aware that this isn't the
# most elegant mechanism to check visited nodes and serves only to verify, but
# wasn't visited. All visited nodes are deleted.
def is_visited(node):
    return not(type(node) is list)


# This solution uses a list of lists (a tuple of a str and a list, to be
# precise) containing the paths of the graph. I'm using the latter with the
# purpose of modify modify the original tree, composing it with previous
# branchs, resulting the original tree with only one key (the root) and
# sub-trees as values.
def build_tree(tree, ls):
    d = dict()
    for elem in ls:

        if type(elem) is str and elem in tree:

            if not is_visited(tree[elem]):

                if is_leaf(tree[elem]):

                    d[elem] = dict()
                else:
                    d[elem] = build_tree(tree, tree[elem])

            else:
                d[elem] = tree[elem]

            # removing previous visited nodes
            del tree[elem]

        elif type(elem) is tuple:

            key, value = elem

            d[key] = build_tree(tree, value)

            # if the return subtree has children
            if len(d[key]) > 0:
                tree[key] = d[key]

            del d[key]

    return d


def add_tree_weights(tree, table):

    lst = []
    if len(tree) == 0:
        return lst

    for key, value in tree.items():
        lst.append(tuple([key, table[key], add_tree_weights(value, table)]))

    return lst


def most_and_least_freq(lst):
    d = dict()

    for elem in lst:
        d[elem] = d.get(elem, 0) + 1
    maximum = max(d.values())
    minimum = min(d.values())

    key_max = 0
    key_min = 0
    for key, value in d.items():
        if value == maximum:
            key_max = key
        elif value == minimum:
            key_min = key
    return key_max, key_min


def tree_balance(tree, table):

    lst_weights = []
    lst_keys = []
    if len(tree) == 0:
        return 0

    for key, weight, elem in tree:

        weight += tree_balance(elem, table)
        lst_weights.append(weight)
        lst_keys.append(key)

    if (max(lst_weights) - min(lst_weights)) != 0:
        most_freq, least_freq = most_and_least_freq(lst_weights)
        unbalanced_index = lst_weights.index(least_freq)
        unbalanced_node = lst_keys[unbalanced_index]
        print('Name', unbalanced_node)
        print('Wrong weight', table[unbalanced_node])
        wrong_diff = abs(most_freq - least_freq)
        print('Correct weight', table[unbalanced_node] - wrong_diff)
        del lst_weights[unbalanced_index]
        lst_weights.append(most_freq)

    return sum(lst_weights)


def main():

    f = open('input.txt')

    tree = dict()
    tree_weights = dict()
    table = dict()
    path = []

    for line in f:
        program_info = line.replace('\n', '').split("->")
        program = program_info[0].split()

        name = program[0]
        weight = eval(program[1])
        adjacency = []
        if len(program_info) >= 2:
            adjacency = program_info[1].replace(' ', '').split(',')

        if len(adjacency) > 0:
            path.append((name, adjacency))
        tree[name] = adjacency
        table[name] = weight

    build_tree(tree, path)

    tree_weights = add_tree_weights(tree, table)
    print('Total balanced weight', tree_balance(tree_weights, table))


if __name__ == "__main__":
    main()
