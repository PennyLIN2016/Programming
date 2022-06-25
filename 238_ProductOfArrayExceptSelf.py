class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 348 ms, faster than 23.98% of Python online submissions for Product of Array Except Self.
        # Memory Usage: 23.6 MB, less than 16.51% of Python online submissions for Product of Array Except Self.
        # time: o(3* n = n) space: o(n)
        l = len(nums)
        lefts = [0] * l
        rights = [0] * l
        res = [0]* l
        for i in range(l):
            if i == 0:
                lefts[0] = nums[0]
            else:
                lefts[i] = lefts[i-1]*nums[i]
        for i in range(l-1, -1, -1):
            if i == l-1:
                rights[i] = nums[i]
            else:
                rights[i] = rights[i+1]*nums[i]
        for i in range(l):
            if i == 0:
                res[i] = rights[i+1]
            elif i == l-1:
                res[i] = lefts[i-1]
            else:
                res[i] = lefts[i-1] * rights[i+1]

        return res






obj = Solution()
t1 =  [1,4]
#t1 = "1-11"
print(t1)
print(obj.productExceptSelf(t1))
