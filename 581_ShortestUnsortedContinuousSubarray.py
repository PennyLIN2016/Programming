class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 180 ms, faster than 87.55% of Python online submissions for Shortest Unsorted Continuous Subarray.
        # Memory Usage: 12.8 MB, less than 33.33% of Python online submissions for Shortest Unsorted Continuous Subarray.
        # my own solution: time o(nllgn)
        sortedList= sorted(nums)
        i,j=0,len(nums)-1
        while i<len(nums) and nums[i] == sortedList[i]:
            i+=1
        if i==len(nums):return 0
        while j>=0 and nums[j] == sortedList[j]:
            j-=1
        return j-i+1

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n=  [2]

    print('---Start---')
    print (n)
    r = object.findUnsortedSubarray(n)
    print(r)
    print('---End---')