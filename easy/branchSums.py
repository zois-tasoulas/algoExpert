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


def branch_sum(root):
    if root:
        return branch_sum_helper(root, 0)
    else:
        raise Exception("Empty root node provided")


def branch_sum_helper(root, current_sum):
    if not root:
        return []

    if (not root.left) and (not root.right):
        return [current_sum + root.value]
    else:
        sum_list = branch_sum_helper(
            root.left, current_sum + root.value
        ) + branch_sum_helper(root.right, current_sum + root.value)
        return sum_list


def main():
    root = Tree(10)
    root.left = Tree(9)
    root.right = Tree(6)
    root.left.left = Tree(8)
    root.left.right = Tree(7)
    sum_of_branches = branch_sum(root)
    print(sum_of_branches)


if __name__ == "__main__":
    main()
