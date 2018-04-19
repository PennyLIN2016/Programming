class Solution(object):
    # my solution 36s
    def findMin1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

    # a good solution : binary tree research 34s
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = int((start + end)/2)
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid +1
        return nums[end]



if __name__ == '__main__':

    #s = [12,15 ,16 ,17 ,21,25,0 ,1, 2,4,5 ,6 ,7,8,9,10,11,11]
    #s = [1,2]
    s = [0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 11]
    print(s)

    k = Solution()
    r = k.findMin(s)

    print (r)



