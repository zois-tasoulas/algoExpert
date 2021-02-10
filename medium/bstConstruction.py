class BST:
    """
    value : value
    left : BST
    right : BST
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        prev = None
        current = self

        while current:
            prev = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if value < prev.value:
            prev.left = BST(value)
        else:
            prev.right = BST(value)

    def remove(self, value):
        if not self.contains(value):
            raise Exception("Value does not exist in tree")

        current = self
        prev = None

        while current:
            if value < current.value:
                prev = current
                current = current.left
            elif value > current.value:
                prev = current
                current = current.right
            else:
                current.remove_node(prev)
                break

    def remove_node(self, parent):
        if self.left is None or self.right is None:
            # Remove root
            if parent is None:
                if self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                elif self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                else:
                    pass
                    # self.value = None
            elif parent.left == self:
                parent.left = self.left if self.right is None else self.right
            elif parent.right == self:
                parent.right = self.left if self.right is None else self.right
        else:
            self.value = self.right.get_min()
            if self.value == self.right.value:
                self.right.remove_node(self)
            else:
                self.right.remove(self.value)

    def get_min(self):
        current = self
        while current.left:
            current = current.left

        return current.value

    def contains(self, value):
        current = self

        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    def print_inorder(self):
        self.print_helper()
        print()

    def print_helper(self):
        if self:
            if self.left:
                self.left.print_helper()
                print("-", end="")
            print(self.value, end="")
            if self.right:
                print("-", end="")
                self.right.print_helper()


def main():
    root = BST(5)
    root.insert(15)
    root.insert(3)
    root.insert(1)
    root.insert(25)
    root.insert(2)
    root.insert(2)
    root.insert(14)

    root.print_inorder()

    root.remove(2)
    root.print_inorder()
    print(root.contains(2))
    root.remove(2)
    root.print_inorder()
    root.remove(15)
    root.print_inorder()
    print(root.contains(2))
    root.print_inorder()
    print(root.contains(25))


if __name__ == "__main__":
    main()
