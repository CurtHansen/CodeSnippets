
def deleteFromBST(t, queries):
    for query in queries:
        t = process_query(t, query)

    return t


def process_query(t, query):
    # First locate where query value is in tree.
    print('process_query(): Looking for value {}'.format(query))
    parent_node, target_node, side = find_node_with_value(t, query)
    print('process_query(): Found {}/{}/{}'.format(parent_node, target_node, side))

    if target_node:
        t = remove_node_from_tree(t, target_node, parent_node, side)

    print("process_query(): Returning {}\n".format(t))
    return t


def find_node_with_value(t, value):
    def recursive_search(current_node, parent_node, side):
        if not current_node:
            return None, None, None
        if current_node.value == value:
            return parent_node, current_node, side
        if value < current_node.value and current_node.left:
            parent_result, target_result, parent_side = \
                recursive_search(current_node.left, current_node, 'left')
            if target_result:
                return parent_result, target_result, parent_side
        if value > current_node.value and current_node.right:
            parent_result, target_result, parent_side = \
                recursive_search(current_node.right, current_node, 'right')
            if target_result:
                return parent_result, target_result, parent_side

        return None, None, None

    print('find_node_with_value(): Looking for value {}'.format(value))

    return recursive_search(t, None, None)


def get_side_node(starting_node, parent_node, direction):
    """
    Get either leftmost or righmost node from the specified starting node.
    """

    print('get_side_node(): starting node/dir {}/{}'.format(starting_node.value, direction))

    def recur_search(current_node, current_parent, direction):
        print('recur_search(): current node/dir {}/{}'.format(current_node.value, direction))
        print('recur_search(): node {} has left? {}'.format(current_node.value, current_node.left is not None))
        print('recur_search(): node {} has right? {}'.format(current_node.value, current_node.right is not None))

        if current_node.left and direction == 'left':
            print('recur_search(): for {} going left'.format(current_node.value))
            ans, ans_parent = recur_search(current_node.left, current_node, direction)
            print('recur_search(): for {} returned from left'.format(current_node.value))
            return ans, ans_parent
        if current_node.right and direction == 'right':
            print('recur_search(): for {} going right'.format(current_node.value))
            ans, ans_parent = recur_search(current_node.right, current_node, direction)
            print('recur_search(): for {} returned from right'.format(current_node.value))
            return ans, ans_parent

        print('recur_search(): node {} didnt meet either test'.format(current_node.value))

        return current_node, current_parent

    ans, ans_parent = recur_search(starting_node, parent_node, direction)
    print('get_side_node(): for original node {} returning {}'.format(starting_node.value, ans.value))

    return ans, ans_parent


def remove_node_from_tree(t, target_node, parent_node, side):
    target_node_is_root = False if parent_node else True
    print('remove_node_from_tree(): node {} is root? {}'.format(target_node.value, target_node_is_root))

    # Case One: Leaf node.
    if not target_node.left and not target_node.right:
        print("remove_node_from_tree(): {} case one true".format(target_node.value))
        if target_node_is_root:
            return None
        else:
            if side == 'left':
                parent_node.left = None
            else:
                parent_node.right = None
            return t

    # Case Two A: Left subtree.
    if target_node.left:
        print("remove_node_from_tree(): node {} case two true".format(target_node.value))
        # Identify the rightmost node in the left branch. This is the replacement node.
        # Remove parent's link to this node, since it will be moved in the tree.
        rightmost_node, rightmost_parent = get_side_node(target_node.left, target_node, 'right')
        rightmost_parent.right = None
        print("remove_node_from_tree(): node {} got rightmost node {}".format(target_node.value, rightmost_node.value))
        # Set replacement node's right branch to target node's right branch.
        rightmost_node.right = target_node.right
        # print("remove_node_from_tree(): node {} set replacement {} right to {}".format(target_node.value, rightmost_node.value, target_node.right.value))

        # Set replacement node's leftmost to have left equal to target node's left branch:
        leftmost_node, _ = get_side_node(rightmost_node, rightmost_parent, 'left')
        print(
            "remove_node_from_tree(): taget node {}, target_node.left {}, rightmost_node {} has leftmost_node {}".format(
                target_node.value, target_node.left.value, rightmost_node.value, leftmost_node.value))
        rightmost_node.left = target_node.left
    # Case Two B: Alternative. If we get here, there must be a right branch.
    else:
        print("remove_node_from_tree(): case three is true")
        rightmost_node = target_node.right

    # Attach replacement node to its new parent (if any).
    if target_node_is_root:
        t = rightmost_node
    else:
        if side == 'left':
            parent_node.left = rightmost_node
        else:
            parent_node.right = rightmost_node

    return t


if __name__ == '__main__':
    deleteFromBST({"value": 3,
                   "left": {
                       "value": 2,
                       "left": {
                           "value": 1,
                           "left": None,
                           "right": None
                       },
                       "right": None
                       },
                   "right": {
                       "value": 5,
                       "left": None,
                       "right": None
                       }
                   },
                  [3, 2, 1])