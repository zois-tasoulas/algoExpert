class BinaryTree:
    """
    value: int
    left: BinaryTree
    right: BinaryTree
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print(self):
        queue = [(self, 0)]

        prev_height = queue[0][1]
        while queue:
            if queue[0][0].left is not None:
                queue.append((queue[0][0].left, queue[0][1] + 1))
            if queue[0][0].right is not None:
                queue.append((queue[0][0].right, queue[0][1] + 1))
            if queue[0][1] != prev_height:
                print()
            print(queue[0][0].value, end=" ")
            prev_height = queue[0][1]
            queue.pop(0)

        print()


def swap_subtrees(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left


def invert_binary_tree(root):
    if root is None:
        return

    queue = [root]

    while queue:
        swap_subtrees(queue[0])
        if queue[0].left is not None:
            queue.append(queue[0].left)
        if queue[0].right is not None:
            queue.append(queue[0].right)
        queue.pop(0)


def main():
    root = BinaryTree(5)
    root.left = BinaryTree(4)
    root.right = BinaryTree(6)

    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(2)

    root.right.left = BinaryTree(7)
    root.right.right = BinaryTree(8)

    root.left.right.left = BinaryTree(1)
    root.left.right.right = BinaryTree(0)

    print("Initial tree")
    root.print()

    invert_binary_tree(root)

    print("Inverted tree")
    root.print()


if __name__ == "__main__":
    main()
