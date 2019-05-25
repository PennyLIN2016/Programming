class MyStack(object):
#Runtime: 16 ms, faster than 95.41% of Python online submissions for Implement Stack using Queues.
#Memory Usage: 11.9 MB, less than 24.31% of Python online submissions for Implement Stack using
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack= []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack = [x]+self.stack


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        t= None
        if not self.empty():
            t = self.stack[0]
            self.stack = self.stack[1:]
        return t


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        t= None
        if not self.empty():
            t = self.stack[0]
        return t


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.stack==[]







if __name__ == '__main__':

    stack = MyStack()


    stack.push(1)
    stack.push(2)
    stack.push(9)
    stack.top()
    stack.pop()
    stack.empty()
    print(stack)
    print('---End---')

