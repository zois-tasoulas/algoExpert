class BinaryTree:
    '''
    value: int
    left: BinaryTree
    right: BinaryTree
    '''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def binary_tree_diameter(root):
    return explore_diameter(root)[0]



def explore_diameter(root):
    if root is None:
        return 0, 0

    subtree_diameter = [0, 0]
    subtree_height = [0, 0]

    subtree_diameter[0], subtree_height[0] = explore_diameter(root.left)
    subtree_diameter[1], subtree_height[1] = explore_diameter(root.right)

    current_height = max(subtree_height[0], subtree_height[1]) + 1
    current_diameter = subtree_height[0] + subtree_height[1]
    left_diameter = subtree_diameter[0]
    right_diameter = subtree_diameter[1]
    return max(current_diameter, left_diameter, right_diameter), current_height



def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)

    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    root.right.left= BinaryTree(6)
    root.right.right = BinaryTree(7)

    print(binary_tree_diameter(root))



if __name__ == "__main__":
    main()
