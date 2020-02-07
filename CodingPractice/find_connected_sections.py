"""
Find the number of connected partitions in a graph that is delivered as a series of arrays, where each cell has a letter.
A connected partition is a set of nodes that have the same letter and that can be reached from one another by traveling
either left-right or up-down (but not diagonally).
For example,
input = [
['a','a','a','a','b', c'],
['a','a','a','b','b', c']
['b','a','a','a','b', c']
['b','b','a','a','b', a']
]
has five connected partitions. Among other facts, the 'a' in the bottom right is a different group from those in the
top left.
"""


def get_coords(node,
               direction,
               nrows,
               ncols):

    """

    :param node: 2-tuple of node coordinates
    :param direction: string, one of 'left', 'right', 'up', 'down'
    :param nrows: int, number of rows in matrix
    :param ncols: int, number of cols in matriix
    :return: either None or 2-tuple of coords
    """
    if direction not in ['left', 'right', 'up', 'down']:
        raise ValueError()

    if direction == 'left':
        if node[1] == 0:
            return None
        else:
            return node[0], node[1] - 1

    if direction == 'right':
        if node[1] == ncols - 1:
            return None
        else:
            return node[0], node[1] + 1

    if direction == 'up':
        if node[0] == 0:
            return None
        else:
            return node[0] - 1, node[1]

    if direction == 'down':
        if node[0] == nrows - 1:
            return None
        else:
            return node[0] + 1, node[1]


def create_dictionary(input_array):
    """

    :param input_array: List of lists of letters
    :return: tuple of dictionary, nrwos, ncols
    """

    ncols = None
    nrows = 0
    mydict = {}
    for rowidx, row in enumerate(input_array):
        nrows += 1
        for colidx, cellvalue in enumerate(row):
            mydict[(rowidx, colidx)] = cellvalue
        if not ncols:
            ncols = colidx + 1
        else:
            if ncols != colidx + 1:
                raise ValueError('Inconsistent number of columns')

    return mydict, nrows, ncols


def analyze_graph(input_array):

    mydict, nrows, ncols = create_dictionary(input_array)

    def explore_node(node_coords,
                     required_letter_value):
        """

        :param node_coords: tuple of coordinates
        :param required_letter_value: string
        :return: None
        """
        letter = mydict.get(node_coords, None)
        if letter == required_letter_value:
            del mydict[node_coords]
            for direction in ['left', 'right', 'up', 'down']:
                neighbor_node = get_coords(node_coords, direction, nrows, ncols)
                if neighbor_node:
                    explore_node(neighbor_node, required_letter_value)

    ans = 0
    while len(mydict) > 0:
        ans += 1
        starting_node = list(mydict.items())[0] # get first node in list
        explore_node(starting_node[0], starting_node[1])

    return ans


if __name__ == '__main__':
    myarray = [['a', 'a', 'b', 'a'],
               ['a', 'a', 'c', 'a'],
               ['a', 'a', 'c', 'b']]
    nclusters = analyze_graph(myarray)
    print(nclusters)