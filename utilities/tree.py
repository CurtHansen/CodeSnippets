class BinaryNode(object):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}/{}/{}".format(self.value, self.left, self.right)


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

def main():
    myjson = {
        "value": 5,
        "left": {
            "value": 2,
            "left": {
                "value": 1,
                "left": 'none',
                "right": 'none'
            },
            "right": {
                "value": 3,
                "left": 'none',
                "right": 'none'
            }
        },
        "right": {
            "value": 6,
            "left": 'none',
            "right": {
                "value": 8,
                "left": {
                    "value": 7,
                    "left": 'none',
                    "right": 'none'
                },
                "right": 'none'
            }
        }
    }
    mytree = BinaryTree()
    mytree.construct((myjson))
    return mytree


if __name__ == '__main__':
    mytree = main()
    mytree

