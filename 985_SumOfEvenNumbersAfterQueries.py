class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Runtime: 706 ms, faster than 40.00% of Python online submissions for Sum of Even Numbers After Queries.
        # Memory Usage: 19.8 MB, less than 15.00% of Python online submissions for Sum of Even Numbers After Queries.
        # time: o(max(n, q)) space: o(1) : ignore the res
        evenSum = 0
        for v in nums:
            if v&1 == 0:
                evenSum += v
        res = []
        for v in queries:
            val, i = v[0], v[1]
            print('nums: {}'.format(nums))
            if nums[i] & 1 == 0:
                evenSum -= nums[i]
            nums[i] += val
            if nums[i] & 1 == 0:
                evenSum += nums[i]

            print('i: {} nums[i]: {} val: {} evenSum: {}'
                  .format(i, nums[i], val, evenSum))
            res.append(evenSum)
        return res



obj = Solution()
t1 = [3,2]
t2 = [[4,0],[3,0]]
print(obj.sumEvenAfterQueries(t1, t2))
