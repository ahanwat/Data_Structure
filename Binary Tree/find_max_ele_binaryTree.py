class Node:
    def __init__(self, data):
        self.data = data
        self.right =  None
        self.left = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

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

      def find_max_recursive(root):
       global maxData
        if not root:
         return maxData

        if root.get_data > maxData:
         maxData = root.get_Data()

        find_max_recursive(root.get.left())
        find_max_recursive(root.get.right())
        return maxData        

    
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)   
print(root.find_max_recursive())