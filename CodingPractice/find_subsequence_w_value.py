"""
Find the first subsequence, if any, whose entries sum to a specified value.
"""


import numpy as np


def find_subsequence_w_value(input_array,
                             target_sum):
    n = len(input_array)
    cumsum = 0
    cumsums = dict()

    for i in range(n):
        diff = cumsum + input_array[i] - target_sum
        diff_idx = cumsums.get(diff, None)
        if diff_idx:
            return diff_idx + 1, i
        elif diff == 0:
            return 0, i
        cumsum += input_array[i]
        cumsums[cumsum] = i

    return None, None


if __name__ == '__main__':
    a, b = find_subsequence_w_value(np.array([4, -5, 5, 6, 7, 3, 4, 6, 1]), 11)
    print(a, b)
    a, b = find_subsequence_w_value(np.array([4, -5, 5, 6, 7, 3, 4, 6, 1]), 20)
    print(a, b)
    a, b = find_subsequence_w_value(np.array([4, -5, 5, 6, 7, 3, 4, 6, 1]), 1)
    print(a, b)
    a, b = find_subsequence_w_value(np.array([4, -5, 5, 6, 7, 3, 4, 6, 1]), 4)
    print(a, b)
    a, b = find_subsequence_w_value(np.array([4, -5, 5, 6, 7, 3, 4, 6, 1]), 100)
    print(a, b)
    a, b = find_subsequence_w_value(np.array([5, -5, 5, 6, 7, 3, 4, 6, 1]), 18)
    print(a, b)







