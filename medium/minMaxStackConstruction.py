import math


class Node:
    """
    value : int
    next : Node
    """

    def __init__(self, value):
        self.value = value
        self.prev = None


class Stack:
    """
    stack : List Node
    """

    def __init__(self):
        self.stack = None

    def push(self, value):
        added_node = Node(value)
        if self.stack is None:
            self.stack = added_node
        else:
            added_node.prev = self.stack
            self.stack = added_node

    def pop(self):
        if self.stack is None:
            raise Exception("Tried to pop from empty stack")
        else:
            popped_node = self.stack
            self.stack = self.stack.prev
            popped_node.prev = None

            return popped_node.value

    def print(self):
        if self.stack is None:
            print("Empty stack")
        current = self.stack
        while current.prev:
            print(current.value, end="->")
            current = current.prev

        print(current.value)


class MinMaxStack:
    """
    stack : Stack
    max : Stack
    min : Stack
    """

    def __init__(self):
        self.stack = Stack()
        self.max = Stack()
        self.min = Stack()

    def push(self, number):
        self.stack.push(number)
        self.max.push(max(number, self.getMax()))
        self.min.push(min(number, self.getMin()))

    def pop(self):
        self.max.pop()
        self.min.pop()

        return self.stack.pop()

    def peek(self):
        if self.stack is None:
            raise Exception("Stack is empty")
        else:
            return self.stack.stack.value

    def getMax(self):
        if self.max.stack is None:
            return -math.inf
        else:
            return self.max.stack.value

    def getMin(self):
        if self.min.stack is None:
            return math.inf
        else:
            return self.min.stack.value

    def print(self):
        self.stack.print()


def main():
    stack = MinMaxStack()
    stack.push(13)
    stack.print()
    stack.push(14)
    stack.print()
    print("min:", stack.getMin())
    print("max:", stack.getMax())
    stack.push(15)
    stack.print()
    print("pop:", stack.pop())
    print("peek:", stack.peek())
    print("pop:", stack.pop())
    print("min:", stack.getMin())
    print("max:", stack.getMax())


if __name__ == "__main__":
    main()
