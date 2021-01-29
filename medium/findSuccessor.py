class BinaryTree:
    """
    value: int
    left: BinaryTree
    right: BinaryTree
    parent: BinaryTree
    """

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def traverse_in_order(root, array):
    if root is None:
        return

    traverse_in_order(root.left, array)
    array.append(root)
    traverse_in_order(root.right, array)


def find_successor(root, node):
    if root is None:
        raise Exception("Empty tree passed to find_successor")

    in_order_nodes = []
    traverse_in_order(root, in_order_nodes)

    prev = in_order_nodes[0]
    for index in range(1, len(in_order_nodes)):
        if prev == node:
            return in_order_nodes[index]
        prev = in_order_nodes[index]

    return None


def leftmost_child(root):
    current = root
    while current.left is not None:
        current = current.left

    return current


def rightmost_parent(node):
    if node.parent is None:
        return None
    current_parent = node.parent

    while current_parent.parent is not None:
        if node == current_parent.left:
            break
        current_parent = current_parent.parent

    # Case when there is no successor
    if current_parent.right == node:
        return None

    return current_parent


def find_successor2(root, node):
    if node.right is not None:
        return leftmost_child(node.right)

    return rightmost_parent(node)


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2, root)
    root.right = BinaryTree(3, root)

    root.left.left = BinaryTree(4, root.left)
    root.left.left.left = BinaryTree(4, root.left)
    root.left.right = BinaryTree(5, root.left)

    root.right.left = BinaryTree(6, root.right)
    root.right.right = BinaryTree(7, root.right)

    print(find_successor2(root, root.left.right))


if __name__ == "__main__":
    main()
