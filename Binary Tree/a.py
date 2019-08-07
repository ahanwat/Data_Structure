import heapq
class Heap:
    def __init__(self):
        self.heaplist =[0]
        self.size = 0
    def parent(self, index):
        return index // 2
    def left_child_index(self, index):
        return 2 * index
    def right_child_index(self, index):
        return 2 * index +1
    def lef_child(self, index):
        if 2 * index <= self.size:
            return self.heaplist[2 * index]
        return -1
    def right_child(self, index):
        if 2 * index + 1 <= self.size:
            return self.heapList[2 * index + 1]
        return -1
    def search_element(self, item):
        i = 1
        while (i <= self.size):
            if item == self.heaplist[i]:
                return i
            i += 1
    def get_minimum(self):
        if self.size == 0:
            return -1
        return self.heaplist[1]
    def prelocate_down(self,i):
        while(i * 2) <= self.size:
         minimum_child = self.minimum_child(i)
         if self.heapist[i]>self.heaplist[minimum_child]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heaplist[minimum_child]
                self.heaplist[minimum_child] = tmp
         i = minimum_child
    def minimum_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heaplist[i * 2]<self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def perlocate_up(self, i):
        while i//2>0:
            if self.heaplist[i]<self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2
    def delet_min(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size = self.size - 1
        self.heaplist.pop()
        self.perlocate_down(1)
        return retval
    def insert(self, k):
        self.heaplist.append(k)
        self.size = self.size + 1
        self.perlocate_up(self.size)
    def printHeap(self):
        print(self.heaplist[1:])
HOrig = Heap()
HOrig.insert(1)
HOrig.insert(20)
HOrig.insert(5)
HOrig.insert(100)
HOrig.insert(1000)
HOrig.insert(12)
HOrig.insert(18)
HOrig.insert(16)
HOrig.printHeap()

