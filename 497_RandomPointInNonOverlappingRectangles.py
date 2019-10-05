import random
import bisect

class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        sums = 0
        self.accumulate = []
        for x1, y1, x2, y2 in rects:
            sums += (y2 - y1 + 1) * (x2 - x1 + 1)
            self.accumulate.append(sums)

    def pick(self):
        """
        :rtype: List[int]
        """
        n = random.randint(1, self.accumulate[-1])
        i = bisect.bisect_left(self.accumulate, n)
        x1, y1, x2, y2 = self.rects[i]
        if(i > 0):
            n -= self.accumulate[i - 1]
        n -= 1
        # imange the area is a matrix of n*m : n= x2-x1+1 m = y2-y1+1
        # the point is kind of [i][j]
        return [x1 + n % (x2 - x1 + 1), y1 + n / (x2 - x1 + 1)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

