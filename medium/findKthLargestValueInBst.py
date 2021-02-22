import heapq


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


def find_kth_largest_value_in_bst(root, k):
    min_heap = []

    visiting_queue = [root]
    while visiting_queue:
        current = visiting_queue.pop(0)
        if len(min_heap) < k:
            heapq.heappush(min_heap, current.value)
        elif min_heap[0] < current.value:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, current.value)

        if current.left:
            visiting_queue.append(current.left)
        if current.right:
            visiting_queue.append(current.right)

    return min_heap[0]


def main():
    root = BST(5)
    root.left = BST(4)
    root.right = BST(27)
    root.left.left = BST(2)
    root.left.right = BST(4)
    root.right.left = BST(15)
    root.right.right = BST(29)

    print(find_kth_largest_value_in_bst(root, 5))


if __name__ == "__main__":
    main()
