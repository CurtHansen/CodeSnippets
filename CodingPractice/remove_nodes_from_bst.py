#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

import json
from CodingPractice.BinaryNodeTree import BinaryTree


def deleteFromBST(t, queries, debug=False):
    for query in queries:
        t = process_query(t, query, debug)

    return t


def process_query(t, query, debug=False):
    # First locate where query value is in tree.
    parent_node, target_node, side = find_node_with_value(t, query)

    if target_node:
        if debug:
            print(f'Removing node value {query}')
        t = remove_node_from_tree(t, target_node, parent_node, side)
    elif debug:
        print(f'Failed to find {query} in tree.')

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

    return recursive_search(t, None, None)


def get_side_node(starting_node, parent_node, direction):
    """
    Get either leftmost or righmost node from the specified starting node.
    """

    def recur_search(current_node, current_parent, direction):

        if current_node.left and direction == 'left':
            ans, ans_parent = recur_search(current_node.left, current_node, direction)
            return ans, ans_parent
        if current_node.right and direction == 'right':
            ans, ans_parent = recur_search(current_node.right, current_node, direction)
            return ans, ans_parent

        return current_node, current_parent

    ans, ans_parent = recur_search(starting_node, parent_node, direction)

    return ans, ans_parent


def remove_node_from_tree(t, target_node, target_parent, side):
    target_node_is_root = False if target_parent else True

    # Case One: Leaf node.
    if not target_node.left and not target_node.right:
        # If the target node is a leaf node, and
        #  1) node is also the root, then it is the only node in the tree so return None
        #  2) node is not root, just disconnect it from parent to drop it
        if target_node_is_root:
            return None  # Node is both a leaf and the root, so just return None.
        else:
            if side == 'left':
                target_parent.left = None
            else:
                target_parent.right = None
            return t

    # Case Two A: Left subtree.
    if target_node.left:
        # Identify the rightmost node in the left branch of the target node.
        # This is the replacement node.
        # To make the move, set
        #  1) replacement's right to target's right.
        #  2) (potentially) replacement's leftmost to target's left
        #  3) replacement parent's right to None (to remove link to replacement).
        #  4) target parent's (if any) right equal to replacement node.
        replacement_node, replacement_parent = get_side_node(target_node.left, target_node, 'right')

        # Set replacement node's right branch to target node's right branch.
        replacement_node.right = target_node.right

        # Set replacement node's leftmost to have left equal to target node's left branch:
        leftmost_under_replacement, _ = get_side_node(replacement_node, replacement_parent, 'left')

        if leftmost_under_replacement.value > target_node.left.value:
            leftmost_under_replacement.left = target_node.left

        # Set replacement_parent's right to point to None (to sever link).
        replacement_parent.right = None

        # Set target's parent (if any) right to replacement node.
        if target_parent:
            if side == 'left':
                target_parent.left = replacement_node
            else:
                target_parent.right = replacement_node

    # Case Two B: Alternative. If we get here, there must be a right branch.
    else:
        replacement_node = target_node.right

    # Attach replacement node to its new parent (if any).
    if target_node_is_root:
        t = replacement_node
    else:
        if side == 'left':
            target_parent.left = replacement_node
        else:
            target_parent.right = replacement_node

    return t


def print_node_details(node):
    node_value = node.value if node else None
    left_value = node.left.value if node.left else None
    right_value = node.right.value if node.right else None
    print('\tprint_node_details() :: node/left/right: {}/{}/{}'.
          format(node_value, left_value, right_value))


if __name__ == '__main__':

    # Get data from JSON.
    with open('/Users/curt//Downloads/test-9.json', 'r') as read_file:
        mydict = json.load(read_file)

    tree = BinaryTree()
    tree.construct(mydict['input']['t'])
    print("\nTree is binary before?: {}".format(tree.test_if_bst()))
    tree.print_all_node_values()

    queries = mydict['input']['queries']
    result_root = deleteFromBST(t=tree.root, queries=queries, debug=True)
    tree.root = result_root
    print("\nTree is binary after?: {}".format(tree.test_if_bst()))
    tree.print_all_node_values()
