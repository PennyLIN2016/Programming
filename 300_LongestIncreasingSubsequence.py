class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 936 ms, faster than 43.07% of Python online submissions for Longest Increasing Subsequence.
        #Memory Usage: 11.8 MB, less than 93.08% of Python online submissions for Longest Increasing
        # time : o(nlgn) space: o(n)
        if not nums: return 0
        dp= [1]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            tmp=1
            for j in range(i):
                if nums[j]<nums[i]:
                    # there is one possible of IS. the length is dp[j]+1
                    tmp=max(tmp,dp[j]+1)
            # get the max of all possilbe IS
            dp[i]=tmp
        # get max of all position, notes: the dp[-1] may not be the answer.
        return max(dp)





if __name__ == '__main__':
    k = Solution()
    s = [10,9,2,5,3,7,101,18]
    print s
    r = k.lengthOfLIS(s)

    print(r)
    print('---End---')



