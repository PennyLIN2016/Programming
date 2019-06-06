class Solution(object):
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 128 ms, faster than 37.45% of Python online submissions for Missing Number.
        # Memory Usage: 12.8 MB, less than 41.73% of Python online submissions for Missing Number.
        # time: O（nlogn）space: o(1)
        # assuming the nums is always not none.
        nums.sort()

        for i in range(len(nums)):
            # ^ is more effective
            if nums[i]!=i:
                return i

        return i+1
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 108 ms, faster than 75.54% of Python online submissions for Missing Number.
        # Memory Usage: 12.5 MB, less than 96.02% of Python online submissions for Missing Number.
        # assuming the missing number is always there. the correct nums is [0...n-1]  but the actual nums is [...n]
        # math solution should be more effective
        l= len(nums)
        cur_sum= sum(nums)
        # the sum of 0..n. the correct : 0-n-1
        excepted_sum = int(l*(l+1)/2)
        return excepted_sum-cur_sum

if __name__ == '__main__':
    s= [9,6,4,2,3,5,7,0,1]

    p = Solution()
    print(p.missingNumber(s))
