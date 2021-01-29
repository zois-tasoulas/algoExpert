class Tree:
    """
    A class to describe a tree node.

    value: int
    right: tree
    left: tree
    """

    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


def find_closest_value_in_bst(root, target):
    if root:
        return find_closest_value_in_bst_helper(root, target, root.value)
    else:
        raise Exception("Empty tree root")


def find_closest_value_in_bst_helper(root, target, closest):
    while root:
        if abs(root.value - target) < abs(target - closest):
            closest = root.value

        if target < root.value:
            root = root.left
        elif target > root.value:
            root = root.right
        else:
            break

    return closest


def main():
    value = 10
    root = Tree(5)
    root.left = Tree(3)
    root.right = Tree(16)
    closest_value = find_closest_value_in_bst(root, value)
    print(closest_value)


if __name__ == "__main__":
    main()
