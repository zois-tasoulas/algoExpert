class BinaryTree:
    """
    value: int
    left: BinaryTree
    right: BinaryTree
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def height_balanced_binary_tree(root):
    if root is None:
        return True

    return (
        height_balanced_binary_tree(root.left)
        and height_balanced_binary_tree(root.right)
        and abs(height(root.left) - height(root.right)) <= 1
    )


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def main():
    root = BinaryTree(5)

    root.left = BinaryTree(6)
    root.right = BinaryTree(7)

    root.left.left = BinaryTree(8)
    root.left.right = BinaryTree(9)

    root.right.left = BinaryTree(10)

    print(height_balanced_binary_tree(root))


if __name__ == "__main__":
    main()
