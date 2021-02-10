class BST:
    """
    value : value
    left : BST
    right : BST
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_inorder(self):
        self.print_helper()
        print()

    def print_helper(self):
        if self:
            if self.left:
                self.left.print_helper()
                print("-", end="")
            print(self.value, end="")
            if self.right:
                print("-", end="")
                self.right.print_helper()


def validate_bst(root, tree_min=float("-inf"), tree_max=float("inf")):
    if root is None:
        return True

    if root.value >= tree_max or root.value < tree_min:
        return False

    return validate_bst(root.left, tree_min, root.value) and validate_bst(
        root.right, root.value, tree_max
    )


def main():
    root = BST(5)
    root.right = BST(15)
    root.left = BST(3)
    root.left.left = BST(1)
    root.right.right = BST(25)
    root.left.left.right = BST(2)
    root.left.left.right.right = BST(2)
    root.right.left = BST(14)

    root.print_inorder()

    print(validate_bst(root))


if __name__ == "__main__":
    main()
