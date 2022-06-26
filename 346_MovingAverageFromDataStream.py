import collections


class MovingAverage(object):
    # Runtime: 88 ms, faster than 48.01% of Python online submissions for Moving Average from Data Stream.
    # Memory Usage: 16.8 MB, less than 26.99% of Python online submissions for Moving Average from Data Stream.
    # deque solution
    def __init__(self, size):
        """
        :type size: int
        """
        self._dq = collections.deque([])
        self._sum = 0
        self._size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        #time: o(1)
        if len(self._dq) == self._size:
            self._sum -= self._dq.popleft()
            self._dq.append(val)
            self._sum += val
        else:
            self._dq.append(val)
            self._sum += val
        return round(self._sum / float(len(self._dq)), 5)

obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))