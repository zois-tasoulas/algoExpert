class LinkedList:
    """
    value : int
    next : LinkedList
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self):
        current = self

        if not current:
            print("Empty list")
            return

        while current.next:
            print(current.value, end="->")
            current = current.next

        print(current.value)

    def add_at_end(self, node):
        current = self
        while current.next:
            current = current.next

        current.next = node


def remove_kth_node_from_end(head, k):
    tail = head
    for _ in range(1, k):
        tail = tail.next

    remove_next = None
    to_remove = head
    while tail.next is not None:
        tail = tail.next
        remove_next = to_remove
        to_remove = to_remove.next

    if remove_next is None:
        # Not checking if head.next exists, list expected to have at least two elements from
        to_remove = to_remove.next
        head.value = head.next.value
        head.next = head.next.next
        to_remove.next = None
    else:
        remove_next.next = to_remove.next
        to_remove.next = None


def main():
    head = LinkedList(10)
    head.add_at_end(LinkedList(11))
    head.add_at_end(LinkedList(12))
    head.add_at_end(LinkedList(13))
    head.add_at_end(LinkedList(14))
    head.add_at_end(LinkedList(15))

    remove_kth_node_from_end(head, 5)
    head.print()
    remove_kth_node_from_end(head, 4)
    head.print()


if __name__ == "__main__":
    main()
