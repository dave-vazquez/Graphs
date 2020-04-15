from graph import Graph
from util import Stack, Queue
import pprint
p_print = pprint.PrettyPrinter(width=30).pprint


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    all_paths = graph.dft_paths(starting_node)

    if len(all_paths) == 1:
        return -1

    longest_path = all_paths[len(all_paths)]

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
