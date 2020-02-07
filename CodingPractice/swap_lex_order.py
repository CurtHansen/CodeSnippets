"""
Given a string str and array of pairs that indicates which indices in the string can be swapped,
    return the lexicographically largest string that results from doing the allowed swaps.
    You can swap indices any number of times.

Example

    For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
    swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca".
The lexicographically largest string in this list is "dbca".

[input] string str
A string consisting only of lowercase English letters.
Guaranteed constraints:
1 ≤ str.length ≤ 104.
[input] array.array.integer pairs
An array containing pairs of indices that can be swapped in str (1-based). This means that for each pairs[i],
    you can swap elements in str that have the indices pairs[i][0] and pairs[i][1].
Guaranteed constraints:
0 ≤ pairs.length ≤ 5000,
pairs[i].length = 2.

[output] string


Input:
str: "abcdefgh"
pairs:
[[1,4],
 [7,8]]

"""


def swapLexOrder(string,
                 pairs):

    n = len(string)

    # Set up maps.
    parent_groups = dict([(x, x) for x in range(n)])  # initially, each group is its own parent

    # Using pairs, identify group clusters.
    for pair in pairs:
        x, y = pair[0] - 1, pair[1] - 1
        # Need to merge the groups of x and y.
        parent_group_x = parent_groups[x]
        parent_group_y = parent_groups[y]
        if parent_group_x == parent_group_y:  # nothing to do
            continue
        subsuming_group, subsumed_group = min(parent_group_x, parent_group_y), \
                                          max(parent_group_x, parent_group_y)  # subsuming group always lowest
        # Move all subsumed group entries to subsuming group.
        for pos in parent_groups:
            if parent_groups[pos] == subsumed_group:
                parent_groups[pos] = subsuming_group

    # Using group clusters, create connected components.
    groups = dict()
    for pos, parent_group in parent_groups.items():
        if groups.get(parent_group, None):
            groups[parent_group] += [pos]
        else:
            groups[parent_group] = [pos]

    # Construct string.
    ans = [None] * n
    for group, groupmembers in groups.items():
        relevant_chars = [string[x] for x in groupmembers]
        relevant_chars = sorted(relevant_chars, reverse=True)
        for idx in range(len(groupmembers)):
            ans[groupmembers[idx]] = relevant_chars[idx]

    ans = "".join(ans)

    return ans


if __name__ == '__main__':
    print(swapLexOrder("abcdefgh",
                       [[1, 4], [7, 8]]))
