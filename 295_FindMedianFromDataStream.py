import heapq


class MedianFinder1(object):
    # the solution is wrong. because The median is the middle value in an ordered integer list.
    # should sort the list before getting median number

    def __init__(self):
        self._list = []
        self._count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self._list.append(num)
        self._count += 1


    def findMedian(self):
        """
        :rtype: float
        """
        #print('list: {} count: {}'.format(self._list, self._count))
        if self._count % 2 == 0:
            return (self._list[self._count/2 - 1] + self._list[self._count/2])/float(2)
        else:
            return self._list[self._count/2]
class MedianFinder(object):
    import heapq
    # Runtime: 1375 ms, faster than 38.05% of Python online submissions for Find Median from Data Stream.
    # Memory Usage: 38.9 MB, less than 23.59% of Python online submissions for Find Median from Data Stream.
    # maxheap + minheap solution
    def __init__(self):
        # the median numbers should be the tops of the two heap
        # the right of the sorted list
        self._smallHeap = []
        # the left of the sorted list
        self._largeHeap = []
        self._smallSize = 0
        self._largeSize = 0
        print('small: {} large: {}'.format(self._smallHeap, self._largeHeap))

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # time: o(nlgn)
        if self._smallSize == 0 and self._largeSize == 0:
            heapq.heappush(self._smallHeap, num)
            self._smallSize += 1
            print('num: {} small: {} large: {} self._largeSize: {} self._smallSize: {}'
                  .format(num, self._smallHeap, self._largeHeap, self._largeSize, self._smallSize))
            return
        if self._smallSize > 0:
            right = self._smallHeap[0]
        if self._largeSize > 0:
            left = -self._largeHeap[0]

        if self._smallSize == self._largeSize:
            # add the nubmer into small heap
            if num < left:
                tmp = heapq.heappushpop(self._largeHeap, -num)
                heapq.heappush(self._smallHeap, -tmp)
            else:
                heapq.heappush(self._smallHeap, num)
            self._smallSize += 1
        elif self._smallSize > self._largeSize:
            # add the number into large heap
            if num > right:
                tmp = heapq.heappushpop(self._smallHeap, num)
                heapq.heappush(self._largeHeap, -tmp)
            else:
                heapq.heappush(self._largeHeap, -num)
            self._largeSize += 1
        print('num: {} small: {} large: {} self._largeSize: {} self._smallSize: {}'
              .format(num, self._smallHeap, self._largeHeap, self._largeSize, self._smallSize))

    def findMedian(self):
        """
        :rtype: float
        """
        # time: o(1)
        print('small: {} large: {}'.format(self._smallHeap, self._largeHeap))
        if self._smallSize == self._largeSize:
            print('1')
            return (self._smallHeap[0] - self._largeHeap[0]) /float(2)
        elif self._smallSize > self._largeSize:
            print('2')
            return float(self._smallHeap[0])

obj = MedianFinder()
obj.addNum(6)
obj.addNum(10)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(15)
print(obj.findMedian())
