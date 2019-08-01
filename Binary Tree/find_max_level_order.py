class Queue(object):

  def __init__(self, limit=5):
    self.que = [];
    self.limit = limit;
    self.front = None;
    self.rear = None;
    self.size = 0;

  def is_empty(self):
    return self.size <= 0;

  def en_queue(self, item):
    if self.size >= self.limit:
      print("Queue Overflow");
    else:
      self.que.append(item)
    if self.front is None:
      self.front = self.rear = 0
    else:
      self.rear = self.size
    self.size += 1
    print("queue afte an en_queue",self.que)

  def de_queue(self):
    if self.size <= 0:
     print("queue underflow")
     return 0
    else:
      self.que.pop(0)
      self.size -= 1
      if self.size == 0:
        self.front = self.rear = 0
      else:
         self.rear = self.size - 1
      print("queue after de+queue", self.que)

  def queue_rear(self):
    if self.rear is None:
      print('sorry queue is empty')
      raise IndexError
    return self.que[self.rear]

  def queue_front(self):
    if self.front is None:
      print('sorry queue is empty')
      raise IndexError
    return self.que[self.front]

  def size(self):
    return self.size

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

    def find_max_using_level_order(root):
        if root is None:
            return
        q =Queue()
        q.en_queue(root)
        node = None
        maxElement = 0
        while not q.is_empty():
            node = q.de_queue()

            if maxElement < node.get_data():
                maxElement = node.get_data()
            if node.left is not None:
                q.en_queue(node.left)
            if node.right is not None:
                q.en_queue(node.right)
        print(maxElement)

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(19)
root.insert(31)
root.insert(42)
Node.find_max_using_level_order(root)