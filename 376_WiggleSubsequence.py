
class Solution(object):
    def wiggleMaxLength1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 12 ms, faster than 98.24% of Python online submissions for Wiggle Subsequence.
        #Memory Usage: 11.7 MB, less than 82.86% of Python online submissions for Wiggle Subsequence.
        # dp solution: time : o(n) space: o(n)
        if not nums: return 0
        if len(nums)==1: return 1

        dp=[[1,0]]*len(nums)
        if nums[0]> nums[1]: dp[1]=[2,1]
        elif nums[0]< nums[1]: dp[1]=[2,-1]
        else:dp[1]=[1,0]
        for i in range(2,len(nums)):
            if dp[i-1][1]==-1:
                if nums[i-1]>nums[i]: dp[i]=[dp[i-1][0]+1,1]
                else : dp[i]=dp[i-1]
            elif dp[i-1][1]==1:
                if nums[i-1]<nums[i]: dp[i]=[dp[i-1][0]+1,-1]
                else: dp[i]=dp[i-1]
            else:
                if nums[i-1]<nums[i]: dp[i]=[dp[i-1][0]+1,-1]
                elif nums[i-1]>nums[i]: dp[i]=[dp[i-1][0]+1,1]
                else: dp[i]=dp[i-1]
        for j in range(len(nums)-1,0,-1):
            if dp[j][1]!=0 : return dp[j][0]
        return 1
    def wiggleMaxLength1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp solution: time : o(n) space: o(n)
        if len(nums)<= 1: return len(nums)
        up = [0 for _ in range(len(nums))]
        down = [0 for _ in range(len(nums))]
        up[0], down[0] = 1, 1
        for i in range(1,len(nums)):
            pre, cur = nums[i-1], nums[i]
            if pre == cur:
                up[i] = up[i-1]
                down[i] = down[i-1]
            elif pre> cur:
                down[i] = up[i-1] +1
                up[i] = up[i-1]
            else:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
        return max(down[-1], up[-1])




if __name__ == '__main__':
    object = Solution()
    k =  [1,7,4,9,2,5]

    print k
    r = object.wiggleMaxLength(k)
    print(r)
    print('---End---')
