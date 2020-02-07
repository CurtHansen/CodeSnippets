"""
Sample code to print the powerset of an input set (in the form of a list).
"""

def print_recursively(staticlist, lenstaticlist, running_subset, level):

    if level == lenstaticlist:
        print(running_subset)

    else:
        print_recursively(staticlist, lenstaticlist, running_subset, level+1)
        print_recursively(staticlist, lenstaticlist, running_subset + [staticlist[level]], level+1)


def print_all_subsets_in_pset(inputlist):

    print_recursively(inputlist, len(inputlist), [], 0)


if __name__ == '__main__':
    print_all_subsets_in_pset([1, 2, 3, 4])
