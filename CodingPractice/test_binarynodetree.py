from CodingPractice.BinaryNodeTree import BinaryTree


if __name__ == '__main__':

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
            "right": {"value": 2, "left": 'none', "right": 'none'}
        }
    }
    mytree = BinaryTree()
    mytree.construct((myjson))
    print(mytree.test_if_bst())

