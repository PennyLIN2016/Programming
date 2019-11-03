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


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
