class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Runtime: 28 ms, faster than 82.98% of Python online submissions for Combination Sum IV.
        #Memory Usage: 12.1 MB, less than 76.04% of Python online submissions for Combination Sum IV.
        # dp solution: time: o(k*n)  time: o(k)
        if not nums: return 0
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            # the value should be positive
            for value in nums:
                if i >=value:
                    dp[i]+=dp[i-value]
        return dp[-1]





if __name__ == '__main__':
    object = Solution()
    k = [1, 2, 3]
    l=4


    print k
    r = object.combinationSum4(k,l)
    print(r)
    print('---End---')
