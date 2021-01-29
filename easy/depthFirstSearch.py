class Node:
    def __init__(self, name, children=None):
        self.name = name
        if children is None:
            children = []
        self.children = children

    def depth_first_search(self, nodes_array):
        if nodes_array:
            raise Exception("Non empty list provided")

        nodes_array.append(self.name)
        nodes_to_visit = []
        for node in reversed(self.children):
            nodes_to_visit.append(node)
        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            nodes_array.append(current_node.name)
            for node in reversed(current_node.children):
                nodes_to_visit.append(node)

        return nodes_array


def main():
    root = Node(
        "A", [Node("B", [Node("E"), Node("F")]), Node("C"), Node("D", [Node("G")])]
    )
    nodes_array = []
    print(root.depth_first_search(nodes_array))


if __name__ == "__main__":
    main()
