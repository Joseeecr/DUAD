class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def print_structure(self):
        def in_order(node):
            if node is not None:
                in_order(node.left)
                print(node.data, end= " ")
                in_order(node.right)
        in_order(self)

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

root.print_structure()