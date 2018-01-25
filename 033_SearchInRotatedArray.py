class question(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left = 0
        right = len(nums)-1

        while left<= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            if nums[mid]>= nums[left]:
                if nums[left]<= target<= nums[mid]:
                    right = mid-1
                else:
                    left = mid +1
            else:
                if nums[mid] <= target<= nums[right]:
                    left = mid +1
                else:
                    right = mid -1

        return -1

if __name__ == '__main__':

    #List = [1,2,3,4,5,6,7,8]
    #List = [8,7,6,5,4,3,2,1]
    List = [5,6,7,8,0,1,2,4]
    target = 8
    #List = None
    k = question()
    print 'input list  :',List, ' + Target: ',target
    r= k.search(List,target)
    print ' Result: ', r



