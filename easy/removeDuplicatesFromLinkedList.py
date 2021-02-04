class List:
    """
    value : int
    next : List
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def print(self):
        if self is not None:
            head = self
            while head.next is not None:
                print(head.value, end="->")
                head = head.next
            print(head.value)


def remove_duplicates_from_linked_list(head):
    prev = head
    while prev is not None:
        current = prev.next
        while current is not None and prev.value == current.value:
            prev.next = current.next
            current = current.next
        prev = prev.next

    return head


def main():
    head = List(5, List(7, List(7, List(7, List(13, List(13, List(14)))))))
    head.print()
    head = remove_duplicates_from_linked_list(head)

    head.print()


if __name__ == "__main__":
    main()
