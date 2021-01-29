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

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

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


def build_tree_recursive(array, min_index, max_index):
    median = (max_index + min_index) // 2
    root = BST(array[median])
    if median - 1 >= min_index:
        root.left = build_tree_recursive(array, min_index, median - 1)
    if median + 1 <= max_index:
        root.right = build_tree_recursive(array, median + 1, max_index)

    return root


def min_height_bst(array):
    root = build_tree_recursive(array, 0, len(array) - 1)

    return root


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    root = min_height_bst(array)
    root.print()


if __name__ == "__main__":
    main()
