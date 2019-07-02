class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 408 ms, faster than 69.04% of Python online submissions for Largest Divisible Subset.
        #Memory Usage: 11.8 MB, less than 86.00% of Python online submissions for Largest Divisible Subset.
        # dp solution: time : o(n**n) space o(n)

        if not nums: return []
        # easy to travel all numbers
        nums.sort()
        # dp[i]: for nums[i] the max length of divisibleSubset
        dp=[0]*len(nums)
        # pre[i]: for nums[i] the max factor number pos in nums
        pre=[0]*len(nums)
        max_l=0
        max_pos=-1
        for i in range(len(nums)):
            for j in range(i):
                # travel all elements less than nums[i], get the pre[i] and dp[i]
                # trace the max length of divisible subset and the pos
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    pre[i]= j
                    if dp[i]>max_l:
                        max_l= dp[i]
                        max_pos=i
        res=[]
        for k in range(max_l+1):
            res.append(nums[max_pos])
            max_pos= pre[max_pos]
        return res


if __name__ == '__main__':
    k = Solution()
    x =[1,2,4,8]


    r = k.largestDivisibleSubset(x)
    print(r)
    print('---End---')
