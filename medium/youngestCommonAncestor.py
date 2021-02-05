class AncestralTree:
    """
    name : str
    ancestor : AncestralTree
    """

    def __init__(self, name, ancestor=None):
        self.name = name
        self.ancestor = ancestor


def youngest_common_ancestor(root, descendant_a, descendant_b):
    ancestors_of_a = {}

    current = descendant_a
    while current is not None:
        ancestors_of_a[current.name] = True
        current = current.ancestor

    current = descendant_b
    while current is not None:
        if current.name in ancestors_of_a:
            return current
        current = current.ancestor

    return None


def find_node_depth(node):
    depth = 0
    current = node

    while current is not None:
        depth += 1
        current = current.ancestor

    return depth


def find_ancestor(deep_node, high_node, dif):
    current_deep = deep_node
    for _ in range(dif):
        current_deep = current_deep.ancestor

    current_high = high_node

    while current_high != current_deep:
        current_high = current_high.ancestor
        current_deep = current_deep.ancestor

    return current_high


def youngest_common_ancestor_2(root, descendant_a, descendant_b):
    depth_a = find_node_depth(descendant_a)
    depth_b = find_node_depth(descendant_b)

    if depth_a > depth_b:
        return find_ancestor(descendant_a, descendant_b, depth_a - depth_b)
    else:
        return find_ancestor(descendant_b, descendant_a, depth_b - depth_a)


def main():
    root = AncestralTree("A")

    child_b = AncestralTree("B", root)
    child_c = AncestralTree("C", root)
    child_d = AncestralTree("D", child_b)
    child_e = AncestralTree("E", child_b)
    child_f = AncestralTree("F", child_c)

    print(youngest_common_ancestor_2(root, child_d, child_f))


if __name__ == "__main__":
    main()
