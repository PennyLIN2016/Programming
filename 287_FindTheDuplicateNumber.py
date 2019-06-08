class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 52 ms, faster than 70.84% of Python online submissions for Find the Duplicate Number.
        #Memory Usage: 14.3 MB, less than 9.29% of Python online submissions for Find the Duplicate Number
        #time 0(n) space: O(n) # space should be o(1)
        visited= set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return nums[i]
            visited.add(nums[i])

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 64 ms, faster than 39.40% of Python online submissions for Find the Duplicate Number.
        #Memory Usage: 13.7 MB, less than 33.90% of Python online submissions for Find the Duplicate
        # time : o(nlgn) space: o(1)
        # the nums[i] in [1,n]  bs: to get the range covering the duplicated number
        # the initial range of the duplicate number is [1,n]
        l,r= 1,len(nums)-1
        while(l<r):
            mid = int((l+r)/2)
            count=0
            # that is not a sorted array ,so have to check the whole array every time
            for value in nums:
                if value<=mid:
                    count+=1
            # if there is not duplicate number, the count should == mid.
            if count>mid:
                r=mid
            else:
                l= mid+1
        # l=r
        return l


if __name__ == '__main__':
    s=[1,3,4,2,2]
    object = Solution()
    r = object.findDuplicate(s)

    print(r)
    print('---End---')



