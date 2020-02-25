#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

from CodingPractice.BinaryNodeTree import BinaryTree


def deleteFromBST(t, queries):
    for query in queries:
        t = process_query(t, query)

    return t


def process_query(t, query):
    # First locate where query value is in tree.
    parent_node, target_node, side = find_node_with_value(t, query)

    if target_node:
        t = remove_node_from_tree(t, target_node, parent_node, side)

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
    tree = BinaryTree()
    tree.construct(
        {"value": -348761264,
         "left": {
             "value": -825429040,
             "left": {
                 "value": -976686917,
                 "left": {
                     "value": -981956058,
                     "left": {
                         "value": -998023278,
                         "left": {
                             "value": -998358422,
                             "left": {
                                 "value": -999581661,
                                 "left": {
                                     "value": -999862211,
                                     "left": {"value": -999963773, "left": 'none', "right": 'none'},
                                     "right": {"value": -999618835, "left": 'none', "right": 'none'}
                                     },
                                 "right": {
                                     "value": -999357649,
                                     "left": {
                                         "value": -999382814,
                                         "left": 'none',
                                         "right": 'none'
                                         },
                                     "right": {
                                         "value": -998814090,
                                         "left": 'none',
                                         "right": 'none'
                                         }
                                     }
                                 },
                             "right": {
                                 "value": -998211991,
                                 "left": {
                                     "value": -998245361,
                                     "left": {
                                         "value": -998261431,
                                         "left": 'none',
                                         "right": 'none'
                                         },
                                     "right": {
                                         "value": -998224931,
                                         "left": 'none',
                                         "right": 'none'
                                         }
                                     },
                                 "right": {
                                     "value": -998118656,
                                     "left": {
                                         "value": -998133050,
                                         "left": 'none',
                                         "right": 'none'
                                         },
                                     "right": {
                                         "value": -998036818,
                                         "left": 'none',
                                         "right": 'none'
                                         }
                                     }
                                 }
                             },
                         "right": {
                             "value": -984096674,
                             "left": {
                                 "value": -993780062,
                                 "left": {
                                     "value": -997344052
                                     }
                                 }
                             }
                        }
                    }
                }
            }
        })
    print("Tree is binary before?: {}".format(tree.test_if_bst()))
    tree.print_all_node_values()
    queries = [-942765665, -942765799, -942765737, -942765498, 962368765, 235142701, -714600801,
               -982067056, 964682986, -761033710, 310778828, -827890484, 857499512, 839480959, 955426856,
               -167019043, -944237440, -942765469, -942765755, 656603678, -942765839, 671700394, -476502379,
               808433215, -942765485, -942765577, -331908252, -942765350, -999382814, 791787847, 342619150,
               -639529093, 433793200, -942765668, 298090578, -942765622, 825468534, -769677309, 508148726,
               118384372, -693287205, -652515683, -315716303, 924893700, 534067828, -942765506, -942765748,
               -785066678, 749739118, -655911547, -453449372, -976929768, -485673863, -942765512, -941092796,
               -942765589, -942765848, 42080873, -807853592, -942765647, 999792215, -654181579, -981902698,
               -201505833, 71733414, -942765546, -330636437, -852265269, 537933165, -942765334, -945679402,
               -766602683, 421602203, -824328207, 925144665, 612771300, -479966609, -253189773, -942765653,
               232193464, -622563971, -697384186, -788097692, -942765399, 338834359, 524573958, -942765619,
               2775195, -942765494, -191430959, -612483461, -942765836, -908777947, -346971194, -777546827,
               333481626, 668866012, -428303986, -942765652, -942765811]
    result_root = deleteFromBST(t=tree.root, queries=queries)
    tree.root = result_root
    print("Tree is binary after?: {}".format(tree.test_if_bst()))
    tree.print_all_node_values()
