class MinHeap:
    """
    heap : List[int]
    """

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        min_heap = array[:]
        self.heap = min_heap

        for index in range(len(min_heap) // 2 - 1, -1, -1):
            self.shiftDown(index)

        return min_heap

    def shiftUp(self):
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[parent], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent],
                )
            else:
                break

            index = parent

    def shiftDown(self, start_point):
        index = start_point
        max_index = len(self.heap) - 1

        while index < max_index:
            child_a = (index + 1) * 2
            child_b = (index + 1) * 2 - 1
            val_parent = self.heap[index]
            if child_a <= max_index:
                val_child_a = self.heap[child_a]
            else:
                val_child_a = val_parent

            if child_b <= max_index:
                val_child_b = self.heap[child_b]
            else:
                val_child_b = val_parent
            min_val = min(val_parent, val_child_a, val_child_b)

            if min_val == val_parent:
                break
            elif min_val == val_child_b:
                self.heap[index], self.heap[child_b] = val_child_b, val_parent
                index = child_b
            else:
                self.heap[index], self.heap[child_a] = val_child_a, val_parent
                index = child_a

    def insert(self, number):
        self.heap.append(number)
        self.shiftUp()

    def remove(self):
        if not self.heap:
            raise Exception("Remove called on empty heap")

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        element = self.heap.pop()
        self.shiftDown(0)

        return element

    def peek(self):
        if not self.heap:
            raise Exception("Peek called on empty heap")

        return self.heap[0]


def main():
    array = [34, 5, 1, 4, 78, 45, 4, 3, 15, 47]
    min_heap = MinHeap(array)
    print(min_heap.heap)
    min_heap.insert(59)
    print(min_heap.heap)
    print(min_heap.remove())
    print(min_heap.heap)
    print(min_heap.peek())
    print(min_heap.heap)
    min_heap.insert(9)
    print(min_heap.heap)
    min_heap.insert(29)
    print(min_heap.heap)


if __name__ == "__main__":
    main()
