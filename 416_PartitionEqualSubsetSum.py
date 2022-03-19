class Solution(object):
    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #89 / 104 test cases passed.Status: Time Limit Exceeded
        # dfs solution:
        def findnext(target,left):
            if not left:
                return False
            if target in left:
                return True
            if target<min(left):
                return False
            for value in left:
                left.remove(value)
                if findnext(target-value,left):
                    return True
                left.add(value)
            return False

        if sum(nums)%2!=0: return False
        return findnext(sum(nums)>>1,nums)
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 24 ms, faster than 97.34% of Python online submissions for Partition Equal Subset Sum.
        #Memory Usage: 11.9 MB, less than 75.00% of Python online submissions for Partition Equal Subset Sum.
        # dfs solution(others)
        def findnext(nums,index,target):
            for i in range(2):
                # the two target can skip impossible numbers, keep the current possible set and try all possible next number 
                if target[i]>=nums[index]:
                    target[i]-=nums[index]
                    if target[i]==0 or findnext(nums,index+1,target): return True
                    target[i]+=nums[index]
            return False
        if sum(nums)%2!=0 or sum(nums)>>1 < max(nums): return False
        # more efficient starting from greater num
        nums.sort(reverse = True)
        target= [sum(nums)>>1]*2
        return findnext(nums,0,target)
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 1283 ms, faster than 55.91% of Python online submissions for Partition Equal Subset Sum.
        #Memory Usage: 13.8 MB, less than 83.29% of Python online submissions for Partition Equal Subset Sum.
        # dp solution: time: o(n*k) space: o(n) k : sum()
        if len(nums)< 2: return False
        total = sum(nums)
        if total%2!=0: return False
        target = total//2
        # dp[i] if there is sunset, which sum is i
        dp = [True] +[False]*target
        # use two loop to choose different combination.
        # skip some value
        for i, v in enumerate(nums):
            # if select v, the sum of other elements is target-v
            # for v, need dp[v]..dp[target]
            for j in range(target,v-1,-1):
                # for j to v
                # count v in
                # dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]] (j >= nums[i])
                dp[j]|= dp[j-v]
                
        return dp[target]
    
    


if __name__ == '__main__':
    object = Solution()
    num = [1, 5, 11, 5,6,8,14,8]

    print(num)
    print('---Start---')
    r = object.canPartition(num)
    print(r)
    print('---End---')
