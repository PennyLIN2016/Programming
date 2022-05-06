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
    
    
    
 import random
class Solution:
    # Runtime: 225 ms, faster than 57.24% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
    # Memory Usage: 18.8 MB, less than 12.50% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
    # time: o(n) space: o(n)
    def __init__(self, rects: list[list[int]]):
        self._rects = rects
        self._start = []
        self._count = 0
        for v in rects:
            self._start.append(self._count)
            self._count += (v[2] - v[0] + 1) * (v[3] - v[1] + 1)
        print('self._start: {} , self._count: {}'
              .format(self._start, self._count))

    def pick(self) -> list[int]:
        target = random.randint(0, self._count-1)
        i = 0
        for i in range(len(self._start)-1, -1, -1):
            print('i: {} self._start[i]: {}'.format(i, self._start[i]))
            if self._start[i] <= target:
                break

        pos = target - self._start[i] + 1
        print('i: {}, target: {} pos: {}'.format(i, target, pos))
        r, c = divmod(pos, self._rects[i][2]-self._rects[i][0] +1)
        print('x: {}, y: {}, mod: {}'.format(r, c, self._rects[i][2]-self._rects[i][0] +1))
        return [self._rects[i][0] + c -1, self._rects[i][1] + r] if c != 0 else [self._rects[i][2], self._rects[i][1] + r -1]





# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

