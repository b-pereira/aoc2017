#!/usr/bin/env python


def traverse_graph(graph, u, visited):

    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            traverse_graph(graph, v, visited)


def main():

    _raw = [ln.strip().split(' <-> ')[1:] for ln in open('input.txt')]

    graph = [[int(d) for d in dgt.split(', ')] for elm in _raw for dgt in elm]

    # part 1
    visited = set()

    traverse_graph(graph, 0, visited)
    total = len(visited)

    print(total)

    # part 2
    total_groups = 1
    previous = 0
    nodes = {v for v in range(len(graph))}

    not_visited = nodes - visited

    while len(not_visited) > 0:
        for u in not_visited:
            traverse_graph(graph, u, visited)

            not_visited = not_visited - visited

            # if the set of not visited nodes has change
            if previous != len(not_visited):
                total_groups += 1
                previous = len(not_visited)

    print(total_groups)


if __name__ == "__main__":
    main()
