import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Less = []# less than median
        self.More = [] # more than median
        self .median = None

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if  self.median == None:
            self.median= num
            return

        if num<= self.median:
            heapq.heappush(self.Less, -num)# the top element is the largest(- element is the least.)
        else:
            heapq.heappush(self.More, num)

        if len(self.Less)> len(self.More)+1:
            top = - heapq.heappop(self.Less)
            heapq.heappush(self.More,self.median)
            self.median = top

        if len(self.More)> len(self.Less)+1:
            top = heapq.heappop(self.More)
            heapq.heappush(self.Less,-self.median)
            self.median = top

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.Less)==len(self.More):
            return self.median
        elif len(self.Less)> len(self.More):
            return (-self.Less[0]+self.median)/2.0
        else:
            return (self.More[0] + self.median)/2.0

if __name__ == '__main__':


    k = MedianFinder()
    for i in xrange(11):
        k.addNum(i)
        print i,' --- median:',k.findMedian()

