class Node:
    """
    name : str
    children: array of Node
    """

    def __init__(self, name, children=None):
        self.name = name
        if children is None:
            self.children = []
        else:
            self.children = children

    def breadth_first_search(self, nodes):
        if len(nodes) > 0:
            raise Exception("Method breadth_first_search expects an empty array")

        to_visit = [self]
        while to_visit:
            visiting_node = to_visit.pop(0)
            to_visit.extend(visiting_node.children)
            nodes.append(visiting_node.name)

        return nodes


def main():
    node_B = Node("B", [Node("D"), Node("E"), Node("F")])
    node_C = Node("C", [Node("G")])
    root = Node("A", [node_B, node_C])
    print(root.breadth_first_search([]))


if __name__ == "__main__":
    main()
