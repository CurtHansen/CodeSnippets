class BinaryNode(object):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}(value/left/right: {}/{}/{})".format(self.__class__.__name__,
                                                       self.value,
                                                       None if not self.left else self.left.value,
                                                       None if not self.right else self.right.value)

    def __str__(self):
        return "value: {}/left: {}/right: {}".format(self.value,
                                                     str(self.left.value) if self.left else None,
                                                     str(self.right.value) if self.right else None)

    def check_bst_condition(self, lower_bound, upper_bound):

        if (lower_bound and self.value < lower_bound) or \
           (upper_bound and self.value > upper_bound):
            return False

        # Check left.
        new_upper_bound = self.value if not upper_bound else min(self.value, upper_bound)
        result_l = True if not self.left else self.left.check_bst_condition(lower_bound, new_upper_bound)
        # Check right.
        new_lower_bound = self.value if not lower_bound else max(self.value, lower_bound)
        result_r = True if not self.right else self.right.check_bst_condition(new_lower_bound, upper_bound)

        return result_l and result_r


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def construct(self, json_details):
        """
        Construct a binary tree based on a json format of node details.

        Parameters
        ----------
        json_details: JSON format dictionary of the form {value: XXX, left: {value: YYY, ...}, right: {value: ZZZ,
            left: ..., right: ...},...}

        Returns
        -------
        None. Populates tree from root node.
        """
        self.root = self.__recur_construct(json_details)

    def __recur_construct(self, json_entry):
        node = BinaryNode(json_entry['value'])
        if isinstance(json_entry['left'], dict):
            node.left = self.__recur_construct(json_entry['left'])
        else:
            node.left = None
        if isinstance(json_entry['right'], dict):
            node.right = self.__recur_construct(json_entry['right'])
        else:
            node.right = None
        return node

    def test_if_bst(self):
        return self.root.check_bst_condition(None, None)


def main():
    myjson = {
        "value": 10,
        "left": {
            "value": 5,
            "left": {"value": 1, "left": 'none', "right": 'none'},
            "right": {
                "value": 7,
                "left": {'value': 6, 'left': 'none', 'right': 'none'},
                "right": {'value': 10, 'left': 'none', 'right': 'none'}
            }
        },
        "right": {
            "value": 15,
            "left": {"value": 11, "left": 'none', "right": 'none'},
            "right": {"value": 20, "left": 'none', "right": 'none'}
        }
    }
    mytree = BinaryTree()
    mytree.construct((myjson))
    return mytree


if __name__ == '__main__':
    mytree = main()
    mytree

