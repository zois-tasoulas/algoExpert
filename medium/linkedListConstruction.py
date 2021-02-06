class Node:
    """
    value : int
    prev : Node
    next : Node
    """

    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt


class DoublyLinkedList:
    """
    head : Node
    tail : Node
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def searchNode(self, node):
        current = self.head
        while current and current != node:
            current = current.next

        return current

    def insertBefore(self, node, nodeToInsert):
        current = self.searchNode(nodeToInsert)

        if current:
            self.remove(current)

        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

        if self.head == node:
            self.head = node.prev

    def insertAfter(self, node, nodeToInsert):
        current = self.searchNode(nodeToInsert)

        if current:
            self.remove(current)

        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

        if self.tail == node:
            self.tail = self.tail.next

    def insertAtPosition(self, position, nodeToInsert):
        if position < 1:
            raise Exception("position should be a positive integer")

        if position == 1:
            self.setHead(nodeToInsert)
        else:
            node = self.head
            for _ in range(1, position):
                if not node:
                    break
                node = node.next

            if not node:
                raise Exception("List shorter than the requested position")

            self.insertBefore(node, nodeToInsert)

    def setHead(self, node):
        if not self.tail and not self.head:
            self.head = node
            self.tail = node
        else:
            if not self.head:
                current = self.tail
                while current.prev:
                    current = current.prev
                self.head = current
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if not self.tail and not self.head:
            self.tail = node
            self.head = node
        else:
            if not self.tail:
                current = self.head
                while current.next:
                    current = current.next
                self.tail = current
            self.insertAfter(self.tail, node)

    def remove(self, node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = None
        node.prev = None

    def removeNodesWithValue(self, value):
        current = self.head

        while current:
            temp = current.next
            if current.value == value:
                self.remove(current)

            current = temp

    def containsNodeWithValue(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def print(self):
        if not self.head:
            print("Empty list")
            return

        current = self.head
        while current.next:
            print(current.value, end="->")
            current = current.next
        print(current.value)
        if self.head:
            if self.tail:
                print("head:", self.head.value, end=" ")
            else:
                print("head:", self.head.value)
        if self.tail:
            print("tail:", self.tail.value)


def main():
    dl_list = DoublyLinkedList()
    dl_list.print()
    node_1 = Node(1)
    dl_list.setHead(node_1)
    dl_list.print()
    node_7 = Node(7)
    dl_list.setTail(node_7)
    dl_list.print()
    node_5 = Node(5)
    dl_list.insertAtPosition(2, node_5)
    dl_list.print()
    node_3 = Node(3)
    dl_list.insertBefore(node_5, node_3)
    dl_list.print()
    node_4 = Node(4)
    dl_list.insertAfter(node_3, node_4)
    dl_list.print()
    dl_list.remove(node_5)
    dl_list.print()
    dl_list.removeNodesWithValue(3)
    dl_list.print()
    print(dl_list.containsNodeWithValue(2))


if __name__ == "__main__":
    main()
