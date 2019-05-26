class MyQueue(object):
#Runtime: 8 ms, faster than 99.70% of Python online submissions for Implement Queue using Stacks.
#Memory Usage: 11.9 MB, less than 9.48% of Python online submissions for Implement Queue usin
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack= []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack=self.stack+[x]


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack==[]: return None
        r = self.stack[0]
        if len(self.stack)>1:
            self.stack=self.stack[1:]
        else:
            self.stack=[]
        return r



    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty(): return None

        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack==[]


if __name__ == '__main__':

    obj = MyQueue()
    obj.push(4)
    obj.push(999)
    obj.push(103)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()

    print(param_3)

    print('---End---')

