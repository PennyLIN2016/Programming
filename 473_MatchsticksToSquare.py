class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 1440 ms, faster than 47.75% of Python online submissions for Matchsticks to Square.
        #Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Matchsticks to Square.
        # dfs solution: travel all possible combinations.
        if not nums or len(nums)<4 :return False
        sumN=sum(nums)
        side,rem=divmod(sumN,4)
        if rem!=0 or max(nums)>side:return False
        sideList=[side]*4
        nums.sort(reverse=True)
        return self.dfs(nums,0,sideList)
    def dfs(self,nums,index,sides):
        if index==len(nums):return True
        num=nums[index]
        for i in range(4):
            if sides[i]>=num:
                sides[i]-=num
                if self.dfs(nums,index+1,sides):return True
                sides[i]+=num
        return False


if __name__ == '__main__':
    object = Solution()
    A=  [1,1,2,2,2]
    print('---Start---')
    r = object.makesquare(A)
    print(r)
    print('---End---')
