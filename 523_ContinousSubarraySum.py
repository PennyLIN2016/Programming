class Solution(object):
    def checkSubarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # brutal solution: 79 / 88 test cases passed. timeout

        if not nums or len(nums)<2: return False
        if k==0 :return False
        for i in range(2,len(nums)+1):
            for j in range(len(nums)-(i-1)):
                tmp=sum(nums[j:j+i])
                if tmp==0:
                    return True
                if tmp%k==0:
                    return True
        return False

    def checkSubarraySum(self, nums, k):
        #Runtime: 200 ms, faster than 41.64% of Python online submissions for Continuous Subarray Sum.
        #Memory Usage: 12.1 MB, less than 75.00% of Python online submissions for Continuous Subarray Sum.
        # time complexity o(n) space complexity o(n)
        # save the pos of the sum for m
        dmap={0:-1}
        total=0
        for i,n in enumerate(nums):
            # sum of [:i]
            total+=n
            m= total%k if k else total
            # a new vaule: dmap[m]: the lest index for m
            if m not in dmap:dmap[m]=i
            # the len>=2 : sum of [m+1:i] %k ==0
            elif dmap[m]+1<i: return True
        return False



if __name__ == '__main__':
    object = Solution()
    A= [23, 2, 4, 6, 7]
    b=6



    print('---Start---')
    print A
    r = object.checkSubarraySum(A,b)
    print(r)
    print('---End---')
