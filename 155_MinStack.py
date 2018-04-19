# a good solution 79s
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.s:
            self.s.append([x, x])
            return
        if x <= self.s[-1][1]:
            self.s.append([x, x])
        else:
            self.s.append([x, self.s[-1][1]])

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s[-1][1]

