import os
os.system("clear")

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def sink_all_islands(islands):
    islands_sunk = 0
    # iterate through each node
    for y in range(0, len(islands)):
        for x in range(0, len(islands[y])):
            # if the node is an island-node
            if islands[y][x] == 1:
                # sink all the connected island-nodes
                islands = sink_island(x, y, islands)
                # and increment the islands sunk by 1
                islands_sunk += 1

    return islands_sunk


def sink_island(x, y, islands):
    # NORTH
    if y > 0:  # if not at northern edge
        # and neighbor is an island-node
        if islands[y-1][x] == 1:
            # sink the island-node by updating it's value to 0
            islands[y-1][x] = 0
            # and visit all it's neighbors
            islands = sink_island(x, y-1, islands)

    # SOUTH
    if y < 4:  # so on, so forth...
        if islands[y+1][x] == 1:
            islands[y+1][x] = 0
            islands = sink_island(x, y+1, islands)

    # EAST
    if x < 4:
        if islands[y][x+1] == 1:
            islands[y][x+1] = 0
            islands = sink_island(x+1, y, islands)

    # WEST
    if x > 0:
        if islands[y][x-1] == 1:
            islands[y][x-1] = 0
            islands = sink_island(x-1, y, islands)

    return islands


islands_sunk = sink_all_islands(islands)

print(f"islands sunk: {islands_sunk}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''
                   INSTRUCTIONS
'''''''''''''''''''''''''''''''''''''''''''''''''''''

# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4
# Keywords
# islands - they consist of connected components
# connected - the neighbors (edges)
# directions - north, south, east, west (edges)
# 2d array - the grap
# returns the number of islands

# How could we write a get neighbor function that uses this shape?
# Offset coordinates, pick a 1 that checks north south east west

# How can we find the extent of an island?
# Either traversal method to find all nodes in island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1
