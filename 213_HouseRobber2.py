class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 20 ms, faster than 75.88% of Python online submissions for House Robber II.
        #Memory Usage: 11.7 MB, less than 69.52% of Python online submissions for House Robber II.
        def subM(subNums):
            if not subNums:
                return 0
            if len(subNums)==1:
                return subNums[0]
            if len(subNums)==2:
                return max(subNums[0],subNums[1])
            m= [0]*len(subNums)
            m[0]=subNums[0]
            m[1]=max(subNums[0],subNums[1])
            for i in range(2,len(subNums)):
                m[i] = max(subNums[i]+m[i-2],m[i-1])
            return m[-1]

        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        # make sure the 0 and -1 be robbed at the same time.
        return max(subM(nums[0:len(nums)-1]),subM(nums[1:len(nums)]))


if __name__ == '__main__':

    t =  [1,3,1,3,100]

    print(t)
    k = Solution()
    r = k.rob(t)

    print(r)
    print('---End---')

