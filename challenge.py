
# from graph import Graph


# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence
# from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# begin_word = "sail"
# end_word = "boat"
# return: ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None


def transformation_sequence(begin_word, end_word):
    graph = Graph()

    if len(begin_word) != len(end_word):
        return None

    # add begin word to graph as a vertex

    # change one letter of the begin_word
        # if resulting string is a word in the word list
        # add it to the graph as an edge

    # recursively transform each new vertex


# hit
# []
