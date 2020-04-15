from graph import Graph
from util import Stack, Queue
import pprint
p_print = pprint.PrettyPrinter(width=30).pprint


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # add the vertices
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    # add the edges, with pair order reversed
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    # get the longest path using new method on graph, dfs_longest_path
    longest_path = graph.dfs_longest_path(starting_node)

    # if there is only one path, ex. [6]
    # there must be no ancestors, therefore
    # return -1
    if len(longest_path) == 1:
        return -1

    # otherwise, return the earliest ancestor of longest path
    return longest_path[-1]


def earliest_ancestor_recursive(ancestors, starting_node):
    # iterate through each ancesto
    for pair in ancestors:
        if pair[1] == starting_node:
            prev_ancestor = earliest_ancestor(ancestors, pair[0])

            if prev_ancestor == -1:
                return pair[0]
            else:
                return prev_ancestor

    return -1
