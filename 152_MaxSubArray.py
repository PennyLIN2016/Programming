class Solution(object):
    # a good solution 56s
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)== 0:
            return 0
        max_num = [0]*len(nums)
        min_num = [0]*len(nums)
        max_num[0]= min_num[0]= nums[0]
        max_pro = nums[0]

        for j in range(1,len(nums)):
            max_num[j] = max(max_num[j-1]*nums[j],nums[j],min_num[j-1]*nums[j])
            min_num[j] = min(max_num[j-1]*nums[j],nums[j],min_num[j-1]*nums[j])
            max_pro = max(max_pro,max_num[j])

        return max_pro


if __name__ == '__main__':

    s = [2,3,-2,4]

    print(s)

    k = Solution()
    r = k.maxProduct(s)

    print (r)



