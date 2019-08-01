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

que = Queue()
que.en_queue("first")
print('Front:',que.queue_front())
print('rear:'+que.queue_rear())
que.en_queue("second")
print('Front:'+que.queue_front())
print('rear:'+que.queue_rear())
que.en_queue("third")
print('Front:'+que.queue_front())
print('rear:'+que.queue_rear())
que.en_queue("fourth")
print('Front:'+que.queue_front())
print('rear:'+que.queue_rear())
que.en_queue("first")
print('Front:',que.queue_front())
print('rear:'+que.queue_rear())



print(que.size)