class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Runtime: 152 ms, faster than 83.22% of Python online submissions for Wiggle Sort II.
        #Memory Usage: 13.1 MB, less than 55.21% of Python online submissions for Wiggle Sort II.
        # O(nlog(n)), S: O(n).
        nums.sort()
        med= int((len(nums)-1)/2)
        print(nums[med::-1])
        print(nums[:med:-1])
        # to avoid the duplicate value break the rule in the list middle.  so the middle number should be put to the different ends of the list.
        nums[::2],nums[1::2]= nums[med::-1],nums[:med:-1]





if __name__ == '__main__':
    k = Solution()
    s=  [1,2,3,4,5,6,7]
    #j = 11

    r = k.wiggleSort(s)

    print(s)
    print('---End---')



