class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 128 ms, faster than 37.45% of Python online submissions for Missing Number.
        # Memory Usage: 12.8 MB, less than 41.73% of Python online submissions for Missing Number.
        # time: o(n) space: o(1)
        # assuming the nums is always not none.
        nums.sort()

        for i in range(len(nums)):
            if nums[i]!=i:
                return i

        return i+1


if __name__ == '__main__':
    s= [1]

    p = Solution()
    print(p.missingNumber(s))