class MyCircularQueue(object):
    # Runtime: 60 ms, faster than 94.61% of Python online submissions for Design Circular Queue.
    # Memory Usage: 12.1 MB, less than 50.00% of Python online submissions for Design Circular Queue.

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.list= [0]*k
        print (self.list)
        self.size,self.len=k,0
        self.head,self.tail=0,0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.len==self.size: return False
        self.list[self.tail] = value
        if self.tail==self.size-1 : self.tail=0
        else: self.tail+=1
        self.len+=1
        return True


    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.len==0: return False
        if self.head==self.size-1: self.head=0
        else: self.head+=1
        self.len-=1
        return True


    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.len==0 :return -1

        return self.list[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.len==0:return -1
        return self.list[self.tail-1] if self.tail!=0 else self.list[-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.len==0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.len==self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(8)
param_1 = obj.enQueue(3)
print(param_1)
param_2 = obj.enQueue(9)
print(param_2)
param_3 = obj.enQueue(5)
print(param_3)
param_4 = obj.enQueue(0)
print(param_4)
param_5 = obj.deQueue()
print(param_5)
param_6 = obj.deQueue()
print(param_6)
param_7 = obj.isEmpty()
print(param_7)
param_8 = obj.isEmpty()
print(param_8)
param_9 = obj.Rear()
print(param_9)
param_10 = obj.Rear()
print(param_10)
param_11 = obj.deQueue()
print(param_11)