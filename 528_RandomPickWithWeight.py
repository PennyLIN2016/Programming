import random
# my own solution : 56 / 57 test cases passed.
class Solution1(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weight=[]
        self.mod=0
        for i,value in enumerate(w):
            self.mod+=value
            self.weight.append([self.mod,i])



    def pickIndex(self):
        """
        :rtype: int
        """
        tmp= random.randint(0,self.mod)
        for value in self.weight:
            if value[0] >= tmp:
                return value[1]

import bisect
# Runtime: 240 ms, faster than 86.25% of Python online submissions for Random Pick with Weight.
#Memory Usage: 16.8 MB, less than 12.50% of Python online submissions for Random Pick with Weight.
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w=w
        self.weight=[0]*len(w)
        for i,value in enumerate(w):
            if i==0:
                self.weight[0]=value
            else:
                self.weight[i]=self.weight[i-1]+value

    def pickIndex(self):
        """
        :rtype: int
        """
        tmp= random.randint(1,self.weight[-1])
        # bisect.bisect_left in a sorted list find the insert position (in front of the position ) time : o(lgn)--  binary search
        return bisect.bisect_left(self.weight,tmp)
    
    import bisect
import random
class Solution1:
    # Runtime: 9681 ms, faster than 5.00% of Python3 online submissions for Random Pick with Weight.
    # Memory Usage: 17.6 MB,less than 99.66% of Python3 online submissions for Random Pick with Weight.
    # time:o(n) space:o(n)
    def __init__(self, w: list[int]):
        tmpSum = sum(w)
        self._freList = [0.0]* (len(w))
        pre = 0.0
        for i, v in enumerate(w):
            self._freList[i] = pre + float(v/tmpSum)
            pre = self._freList[i]

        print('self._freList: {}'.format(self._freList))


    def pickIndex(self) -> int:
        if len(self._freList) == 1:
            return 0
        pos = random.random()
        print('pos: {}'.format(pos))
        i = 0
        while True:
            if self._freList[i] >= pos:
                return i
            i += 1
import bisect
class Solution:
    #Runtime: 288 ms, faster than 62.96% of Python3 online submissions for Random Pick with Weight.
    #Memory Usage: 18.4 MB, less than 78.84% of Python3 online submissions for Random Pick with Weight.
    def __init__(self, w: list[int]):
        self._sum = [w[0]]
        for v in w[1:]:
            self._sum.append(self._sum[-1] + v)

    def pickIndex(self) -> int:
        # Similar to bisect_left(), but returns an insertion point which comes after
        # (to the right of) any existing entries of x in a.
        # time: o(lgn) space: o(n)
        return bisect.bisect(self._sum, self._sum[-1]* random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
