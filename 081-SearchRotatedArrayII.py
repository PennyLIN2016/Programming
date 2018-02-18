class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False


        left = 0
        right = len(nums)-1

        while left<= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return True

            if nums[mid]> nums[left]:
                # the disordered num in the right. the sub-list before the mid is well-ordered.
                if nums[left]<= target< nums[mid]:
                    right = mid-1
                else:
                    left = mid +1
            elif nums[mid]< nums[left]:
                # the disordered num in the left. the sub-list behind the mid is well-ordered.
                if nums[mid] < target<= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            else:
                # the nums after mid and before left are the same or the nums between left and right are the same.  now can not tell where the target is.
                left += 1
        return False

if __name__ == '__main__':

    List = [1,3,1,1,1]
    target = 3
    #List = None
    k = Solution()
    print 'input list  :',List, '  Target: ',target
    r= k.search(List,target)
    print ' Result: ', r




