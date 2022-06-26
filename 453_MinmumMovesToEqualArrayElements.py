class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 254 ms, faster than 64.86% of Python online submissions for Minimum Moves to Equal Array Elements.
        # Memory Usage: 14.4 MB, less than 77.03% of Python online submissions for Minimum Moves to Equal Array Elements.
        # time: o(n) space: o(1)
        minValue = min(nums)
        res = 0
        for v in nums:
            res += v - minValue
        return res

obj = Solution()
t1 = [1,2,3]
#t1 = "1-11"
print(t1)
print(obj.minMoves(t1))


