class Tree:
    '''
    A class to describe a tree node.

    value: int
    right: tree
    left: tree
    '''
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left



def node_depths(tree):
    if tree:
        return node_depths_helper(tree, 0)
    else:
        raise Exception("Tree rood was 'None'")



def node_depths_helper(tree, depth_sum):
    if not tree:
        return 0
    else:
        return depth_sum + node_depths_helper(tree.left, depth_sum + 1) + \
               node_depths_helper(tree.right, depth_sum + 1)



def main():
    root = Tree(5)

    root.right = Tree(25)
    root.left = Tree(6)

    root.right.right = Tree(12)
    root.right.left = Tree(15)

    print(node_depths(root))



if __name__ == "__main__":
    main()
