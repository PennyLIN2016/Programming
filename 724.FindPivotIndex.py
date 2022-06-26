class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 169 ms, faster than 65.50% of Python online submissions for Find Pivot Index.
        # Memory Usage: 14.3 MB, less than 94.55% of Python online submissions for Find Pivot Index.
        # time: o(n) space: o(1)
        if len(nums) == 1:
            return 0 if nums[0] == 0 else -1
        sumRight = sum(nums[1:])
        sumLeft = 0
        for i in range(1, len(nums)+1):
            print('i-1: {} sumRight: {} sumLeft: {}'.format(i-1, sumRight, sumLeft))
            if sumRight == sumLeft:
                return i-1
            if i == len(nums):
                break
            sumRight -= nums[i]
            sumLeft += nums[i-1]
            print('i: {} sumRight: {} sumLeft: {}'.format(i, sumRight, sumLeft))
        return -1


obj = Solution()
t1 = [-1,-1,0,1,1,0]
print(obj.pivotIndex(t1))
