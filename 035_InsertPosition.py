class question(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        left = 0
        right = len(nums)-1

        while left>= 0 and right < len(nums) and left<= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                left = mid+1
            else:
                right = mid -1
        return left

if __name__ == '__main__':

    #List = [1,2,3,6,7,9,10]
    #List = [8,7,6,5,4,3,2,1]
    #List = [1,2,3,7,0,9,4,10,9,8,6]
    #List = None
    List = [1]

    target = 8
    k = question()
    print 'input is :',List
    r= k.searchRange(List,target)
    print ' result: ', r



