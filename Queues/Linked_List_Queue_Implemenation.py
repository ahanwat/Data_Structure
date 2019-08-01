class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.last = None
        self.next = next
    def set_data(self,data):
        self.data = data
    def