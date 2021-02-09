class LinkedList:
    """
    value : int
    next : LinkedList
    """

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def print(self):
        if not self:
            print("Empty list")

        current = self
        while current.next:
            print(current.value, end="->")
            current = current.next

        print(current.value)


def sum_of_linked_lists(list_a, list_b):
    carry = False
    pointer_a = list_a
    pointer_b = list_b

    head_sum = None
    current_sum = head_sum

    while pointer_a or pointer_b:
        value_a = 0 if not pointer_a else pointer_a.value
        value_b = 0 if not pointer_b else pointer_b.value
        new_sum = value_a + value_b
        if carry:
            new_sum += 1
            carry = False

        if new_sum > 9:
            new_sum -= 10
            carry = True

        if not current_sum:
            head_sum = LinkedList(new_sum)
            current_sum = head_sum
        else:
            current_sum.next = LinkedList(new_sum)
            current_sum = current_sum.next

        if pointer_a:
            pointer_a = pointer_a.next
        if pointer_b:
            pointer_b = pointer_b.next

    if carry:
        current_sum.next = LinkedList(1)

    return head_sum


def main():
    root_a = LinkedList(5)
    root_a.next = LinkedList(7)
    root_a.next.next = LinkedList(2)

    root_b = LinkedList(3)
    root_b.next = LinkedList(5)
    root_b.next.next = LinkedList(7)
    root_b.next.next.next = LinkedList(4)

    root_sum = sum_of_linked_lists(root_a, root_b)
    root_sum.print()


if __name__ == "__main__":
    main()
