"""
Find the longest (strictly) increasing subsequence in an unsorted array.
"""

import numpy as np


def determine_length_iss_terminating_at_position(array,
                                                 position,
                                                 length_longest_iss):
    """
    Compute the longest increasing subsequence terminating at position 'position'.
    :param array: Unsorted array/list of length n.
    :param position: Position in array to process. Must be that 0 <= position <= n-1.
    :param length_longest_iss: array whose ith value is the length of longest increasing subsequence
        terminating at that point.
    :return: integer, the length of the longest subsequence terminating at position 'position'.
    """

    # If at the start of the array, trivially return 1.
    if position == 0:
        return 1

    # Compute length of longest iss by using information on predecessors in the list.
    # Do this by looping over all preceding indices and attempting to append the current position to create a new,
    #  longer subsequence.
    length_longest_iss_for_position = 1  # Initialize to 1.
    for prev_idx in range(position):
        if array[prev_idx] < array[position] and length_longest_iss[prev_idx] + 1 > length_longest_iss_for_position:
            length_longest_iss_for_position = length_longest_iss[prev_idx] + 1

    return length_longest_iss_for_position


def determine_length_lis_bottom_up(array):
    """
    Determine the length of the longest increasing subsequence from the bottom up.
    :param array: input array of numbers
    :return: int, the length of the longest subsequence
    """
    n = len(array)
    # Construct container holding the length of the longest increasing subsequence ending at position i for
    # i in [0, n-1].
    max_length_iss_terminating_pos = np.ones(n, int)

    for position in range(n):
        max_length_iss_terminating_pos[position] =\
            determine_length_iss_terminating_at_position(array, position, max_length_iss_terminating_pos)

    return max(max_length_iss_terminating_pos)


if __name__ == '__main__':
    array = np.array([10, 4, 6, 2, 8, 9, 5])
    print(determine_length_lis_bottom_up(array))
    array = np.array(range(10))
    print(determine_length_lis_bottom_up(array))