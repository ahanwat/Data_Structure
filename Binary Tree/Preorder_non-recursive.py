class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Preorder traversal
# Root -> Left ->Right

    def preorder_iterative(root, result):
         if not root:
             return
         stack = []
         stack.append(root)

         while stack:
             node = stack.pop()
             result.append(node.data)
             if node.right:
                 stack.append(node.right)
             if node.left:
                 stack.append(node.left)

root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
print(root.preorder_iterative(root))
