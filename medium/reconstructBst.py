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


def reconstruct_bst(tree):
    if tree == []:
        return None
    root = BST(tree[0])

    right_subtree = len(tree)
    for index in range(1, len(tree)):
        if tree[index] >= tree[0]:
            right_subtree = index
            break

    root.left = reconstruct_bst(tree[1:right_subtree])
    root.right = reconstruct_bst(tree[right_subtree:])

    return root


def main():
    tree = [23, 12, 10, 14, 25, 23, 27, 26, 44]
    print(reconstruct_bst(tree))


if __name__ == "__main__":
    main()
