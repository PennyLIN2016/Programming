class question(object):
    def maxSubArray1(self, nums):# low efficiency
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[:]
        for i in xrange(len(nums)):
            sum_tmp = nums[i]
            for j in xrange(i+1,len(nums)):
                sum_tmp += nums[j]
                if sum_tmp > sum[i]:
                    sum[i] = sum_tmp
        return max(sum)

    def maxSubArray(self, nums): # high efficiency
        pre_max = nums[0]
        max_sum = nums[0]
        for i in xrange(1,len(nums)):
            pre_max= max(pre_max+nums[i],nums[i])
            # the max vaule including the num[i]
            max_sum = max(max_sum,pre_max)
        return max_sum

if __name__ == '__main__':

    k = question()
    List = [-2,1,-3,4,-1,2,1,-5,4]
    #List= [1]
    r= k.maxSubArray(List)
    print r




