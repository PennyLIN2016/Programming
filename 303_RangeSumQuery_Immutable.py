class NumArray1(object):
    ##Runtime: 1008 ms, faster than 14.77% of Python online submissions for Range Sum Query - Immutable.
    #Memory Usage: 15.1 MB, less than 99.53% of Python online submissions for Range Sum Query - Immutable.

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums= nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>j: return 0
        if j>len(self.nums)-1:j=len(nums-1)
        return sum(self.nums[i:j+1])

class NumArray(object):
    #Runtime: 64 ms, faster than 80.58% of Python online submissions for Range Sum Query - Immutable.
    #Memory Usage: 15.5 MB, less than 43.49% of Python online submissions for Range Sum Query - Immutable.

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.sum=[]
        else:
            # self.sum[i]: save the sum of [0,i-1]
            self.sum= [0]*(len(nums)+1)
            for i in range(len(nums)):
                self.sum[i+1]=self.sum[i]+nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>j: return 0
        return self.sum[j+1]-self.sum[i]


if __name__ == '__main__':
    s = [-2, 0, 3, -5, 2, -1]
    k = NumArray(s)
    i=0
    j=2

    print s
    r = k.sumRange(i,j)

    print(r)
    print('---End---')



