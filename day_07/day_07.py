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


def main():

    f = open('input.txt')

    tree = dict()
    path = []

    for line in f:
        program_info = line.replace('\n', '').split("->")
        program = program_info[0].split()
        name = program[0]
        adjacency = []
        if len(program_info) >= 2:
            adjacency = program_info[1].replace(' ', '').split(',')

        if len(adjacency) > 0:
            path.append((name, adjacency))
        tree[name] = adjacency

    build_tree(tree, path)
    print(list(tree.keys())[0])


if __name__ == "__main__":
    main()
