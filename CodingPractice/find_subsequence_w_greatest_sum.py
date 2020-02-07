"""
For an input sequence, find the subsequence with the greatest sum.
Key point is to note that the sum of any subsequence is the entire cumulative sum minus the sum of the preceding
subsequence starting at 0 and ending at the index before the start of the subsequence. In the special case where
the index is 0, there is no such preceding subsequence and the sum of the preceding subsequence can be deemed to be 0.
"""

import numpy as np


def find_subseq_w_greatest_sum(input_array):
    n = len(input_array)
    cum_sum = 0
    end_lowest_seq, val_lowest_seq = -1, 0
    start_greatest_seq, end_greatest_seq, val_greatest_seq = 0, 0, -np.inf

    for i in range(n):
        cum_sum += input_array[i]
        if cum_sum < val_lowest_seq:
            val_lowest_seq = cum_sum
            end_lowest_seq = i
        if cum_sum - val_lowest_seq > val_greatest_seq:
            val_greatest_seq = cum_sum - val_lowest_seq
            start_greatest_seq = end_lowest_seq + 1
            end_greatest_seq = i

    return start_greatest_seq, end_greatest_seq, val_greatest_seq


if __name__ == '__main__':
    a, b, c = find_subseq_w_greatest_sum(np.array([0, 1, 4, -6, 8, 4, 5, 10, 4]))
    print(a, b, c)
    a, b, c = find_subseq_w_greatest_sum(np.array([-30, -1, -4, -6, 8, -4, -5, -10, 4]))
    print(a, b, c)
    a, b, c = find_subseq_w_greatest_sum(np.array([30, 1, 4, 6, 8, -4, 1, 1, 1]))
    print(a, b, c)
    a, b, c = find_subseq_w_greatest_sum(np.array([30, 1, 4, 6, 8, -4, 1, 1, 10]))
    print(a, b, c)
    a, b, c = find_subseq_w_greatest_sum(np.array([30, -1, -4, -6, -8, -4, 1, 1, 10]))
    print(a, b, c)
    a, b, c = find_subseq_w_greatest_sum(np.array([1, -3, 5, -2, 9, -8, -6, 4]))
    print(a, b, c)
