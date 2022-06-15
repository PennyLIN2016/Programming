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
    
    ##### python 3 solution:
     def findUnsortedSubarray(self, nums: list[int]) -> int:
        # Runtime: 314 ms, faster than 43.94% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        # Memory Usage: 15.2 MB, less than 50.53% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        # time: o(nlgn) space: o(n)
        oldNums = nums[:]
        nums.sort()
        left, right = 0, len(nums)-1
        while left <= right and oldNums[left] == nums[left]:
            left += 1
        if left == right+1:
            return 0
        while right >= left and oldNums[right] == nums[right]:
            right -= 1
        return right - left + 1

    def findUnsortedSubarray(self, nums: list[int]) -> int:
        #Runtime: 178 ms, faster than 100.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        #Memory Usage: 15.4 MB, less than 6.70% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
        order = [x == y for x, y in zip(nums, sorted(nums))]
        return 0 if all(order) else (len(nums)) - order.index(False) - order[::-1].index(False)

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n=  [2]

    print('---Start---')
    print (n)
    r = object.findUnsortedSubarray(n)
    print(r)
    print('---End---')
