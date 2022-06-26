class HitCounter(object):
    # Runtime: 15 ms, faster than 94.86% of Python online submissions for Design Hit Counter.
    # Memory Usage: 13.5 MB, less than 39.73% of Python online submissions for Design Hit Counter.

    def __init__(self):
        import collections
        self._hits = collections.deque([])
        self._cntSum = 0
    # tiem: o(1)
    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        while self._hits:
            v = self._hits[0]
            if timestamp - v[0] >= 300:
                self._cntSum -= v[1]
                self._hits.popleft()
            else:
                break

        print('1--timestamp: {} self._hits: {} self._cntSum: {}'
              .format(timestamp, self._hits, self._cntSum))
        if not self._hits or self._hits[-1][0] != timestamp:
            self._hits.append([timestamp, 1])
        else:
            self._hits[-1][1] += 1
        self._cntSum += 1
        print('2--timestamp: {} self._hits: {} self._cntSum: {}'
              .format(timestamp, self._hits, self._cntSum))

    # time: o(1)
    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        while self._hits:
            v = self._hits[0]
            if timestamp - v[0] >= 300:
                self._cntSum -= v[1]
                self._hits.popleft()
            else:
                break
        return self._cntSum

obj = HitCounter()
"""
print(obj.hit(1))
print(obj.hit(2))
print(obj.hit(3))
print(obj.getHits(4))
print(obj.hit(300))
print(obj.getHits(300))
print(obj.getHits(301))
"""
print(obj.hit(1))
print(obj.hit(1))
print(obj.hit(1))
print(obj.hit(300))
print(obj.getHits(300))

