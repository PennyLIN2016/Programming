class MyCircularDeque(object):
    # Runtime: 72 ms, faster than 72.00% of Python online submissions for Design Circular Deque.
    # Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Design Circular Deque.
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.maxSize=k
        self.size=0
        self.stack=[]


    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size>=self.maxSize: return False
        self.stack=[value]+self.stack
        self.size+=1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size>=self.maxSize: return False
        self.stack.append(value)
        self.size+=1
        return True


    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size==0: return False
        self.stack=self.stack[1:]
        self.size-=1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size==0: return False
        self.stack.pop()
        self.size-=1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.size==0: return -1
        return self.stack[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.size==0: return -1
        return self.stack[-1]


    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size==0


    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size==self.maxSize

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(9)
param_1 = obj.insertFront(8)
param_2 = obj.insertLast(16)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()
