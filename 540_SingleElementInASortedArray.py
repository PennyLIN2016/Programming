class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 52 ms, faster than 88.00% of Python online submissions for Single Element in a Sorted Array.
        #Memory Usage: 13.7 MB, less than 7.14% of Python online submissions for Single Element in a Sorted Array.
        #my solution : the result deletel the first line. time :o(n), space:o(1)
        if not nums or len(nums)%2==0 :return None
        if len(nums)==1:return nums[0]
        res=nums[0]^nums[1]
        for i in range(2,len(nums)):
            res^=nums[i]
        return res


if __name__ == '__main__':
    object = Solution()
    n1=[1,1,7,3,3,4,4,8,8]

    print('---Start---')
    print n1
    r = object.singleNonDuplicate(n1)
    print(r)
    print('---End---')
