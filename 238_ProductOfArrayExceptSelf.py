class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #Runtime: 96ms, faster than 90.65 % of Python online submissions for Product of Array Except Self.
        #Memory Usage: 18.3 MB, less than 80.70 % of Python online submissions for Product of Array Except Self.

        res = [1]*len(nums)
        #get the production [0,i-1]
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        #get the production[i+1,-1]
        cur_product = 1
        for j in range(len(nums)-1,-1,-1):
            res[j]= cur_product*res[j]
            cur_product *= nums[j]

        return res



if __name__ == '__main__':
    nums = [1,2,3,4]
    p = Solution()
    print(p.productExceptSelf(nums))