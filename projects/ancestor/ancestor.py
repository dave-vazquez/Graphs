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

    # get all paths where any duplicate lengthed paths
    # are reduced to 1 path with the earliest ancestor of
    # the smallest id
    all_paths = graph.dft_paths(starting_node)

    # if there is only one path, ex. [6]
    # there must be no ancestors, therefore
    # return -1
    if len(all_paths) == 1:
        return -1

    # otherwise select the longest_path using the
    # length of all_paths as the key
    longest_path = all_paths[len(all_paths)]

    # and return the earliest ancestor of that path
    return longest_path[-1]


test_ancestors = [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (8, 9),
    (11, 8),
    (10, 1)
]

# result = earliest_ancestor(test_ancestors, 1)
# result = earliest_ancestor(test_ancestors, 2)
# result = earliest_ancestor(test_ancestors, 3)
# result = earliest_ancestor(test_ancestors, 4)
# result = earliest_ancestor(test_ancestors, 5)
# result = earliest_ancestor(test_ancestors, 6)
# result = earliest_ancestor(test_ancestors, 7)
# result = earliest_ancestor(test_ancestors, 8)
# result = earliest_ancestor(test_ancestors, 9)
# result = earliest_ancestor(test_ancestors, 10)
# result = earliest_ancestor(test_ancestors, 11)

# print(result)

result = earliest_ancestor(test_ancestors, 9)
print(f"result: {result}")

# def earliest_ancestor(ancestors, starting_node):
#     print(f"{starting_node}")
#     for ancestor in ancestors:
#         if ancestor[1] == starting_node:
#             if earliest_ancestor(ancestors, ancestor[0]) == -1:
#                 return ancestor[0]

#     return -1
