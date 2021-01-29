class BST:
    """
    value: int
    left: BST
    right: BST
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_traverse(root, array):
    if root is None:
        return

    in_order_traverse(root.left, array)
    array.append(root.value)
    in_order_traverse(root.right, array)


def post_order_traverse(root, array):
    if root is None:
        return

    post_order_traverse(root.left, array)
    post_order_traverse(root.right, array)
    array.append(root.value)


def pre_order_traverse(root, array):
    if root is None:
        return

    array.append(root.value)
    pre_order_traverse(root.left, array)
    pre_order_traverse(root.right, array)


def main():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(12)

    root.left.left = BST(4)
    root.left.right = BST(8)

    root.right.left = BST(10)
    root.right.right = BST(25)

    in_order = []
    in_order_traverse(root, in_order)
    print(in_order)

    post_order = []
    post_order_traverse(root, post_order)
    print(post_order)

    pre_order = []
    pre_order_traverse(root, pre_order)
    print(pre_order)


if __name__ == "__main__":
    main()
