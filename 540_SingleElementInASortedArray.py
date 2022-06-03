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
    
    def singleNonDuplicate(self, nums):
        # Runtime: 60 ms, faster than 35.77% of Python online submissions for Single Element in a Sorted Array.
        #Memory Usage: 13.6 MB, less than 7.14% of Python online submissions for Single Element in a Sorted Array.
        # my own solution: timeo(n/2)
        #if not nums or len(nums)%2==0 :return None
        if len(nums)==1:return nums[0]
        for i in range(0,len(nums),2):
            if i == len(nums)-1:return nums[i]
            if nums[i]!=nums[i+1]:
                return nums[i]
            
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # Runtime: 362 ms, faster than 5.65% of Python3 online submissions for Single Element in a Sorted Array.
        # Memory Usage: 23.8 MB, less than 12.88% of Python3 online submissions for Single Element in a Sorted Array.
        # time: o(lgn) space: o(1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid % 2 == 0 and nums[mid] == nums[mid + 1]:
               left = mid + 1
            elif mid % 2 == 0 and nums[mid] == nums[mid - 1]:
                right = mid - 1
            elif mid % 2 == 1 and nums[mid] == nums[mid + 1]:
                right = mid -1
            else:
                left = mid + 1
        return nums[right]

if __name__ == '__main__':
    object = Solution()
    n1=[1,1,7,3,3,4,4,8,8]

    print('---Start---')
    print n1
    r = object.singleNonDuplicate(n1)
    print(r)
    print('---End---')
