def get_intersection(array1,
                     array2):

    idx1 = 0
    idx2 = 0
    n1 = len(array1)
    n2 = len(array2)

    ans = list()

    while idx1 < n1 and idx2 < n2:
        if array1[idx1] == array2[idx2]:
            ans.append(array1[idx1])
            idx1 += 1
            idx2 += 1
        elif array1[idx1] > array2[idx2]:
            idx2 += 1
        else:
            idx1 += 1

    return ans


def get_difference(array1,
                   array2):

    idx1 = 0
    idx2 = 0
    n1 = len(array1)
    n2 = len(array2)

    ans = list()

    while True:

        if idx1 < n1 and idx2 < n2:
            if array1[idx1] < array2[idx2]:
                ans.append(array1[idx1])
                idx1 = min(n1, idx1+1)
            elif array1[idx1] > array2[idx2]:
                ans.append(array2[idx2])
                idx2 = min(n2, idx2+1)
            else:
                idx1 = min(n1, idx1+1)
                idx2 = min(n2, idx2+1)

        elif idx1 < n1 and idx2 == n2:
            ans.append(array1[idx1])
            idx1 = min(n1, idx1+1)

        elif idx1 == n1 and idx2 < n2:
            ans.append(array2[idx2])
            idx2 = min(n2, idx2 + 1)

        else:
            break

    return ans


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 6, 9, 10]
    arr2 = [2, 3, 4, 9, 10, 12, 20]
    print(get_intersection(arr1, arr2))
    print(get_difference(arr1, arr2))

