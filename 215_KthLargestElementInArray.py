class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Runtime: 48 ms, faster than 72.54% of Python online submissions for Kth Largest Element in an Array.
        #Memory Usage: 12.4 MB, less than 40.99% of Python online submissions for Kth Largest Element in an Array.
        if not nums: return  0
        nums.sort()
        print(nums)
        return nums[-k]

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Runtime: 64 ms, faster than 55.15% of Python online submissions for Kth Largest Element in an Array.
        #Memory Usage: 12.4 MB, less than 37.47% of Python online submissions for Kth Largest Element in an Array.
        from  heapq import nlargest,heapify
        if not nums: return  0
        heapify(nums)
        return (nlargest(k,nums)[-1])


if __name__ == '__main__':

    t =  [3,2,1,5,6,4]
    s = 2
    print(t)
    k = Solution()
    r = k.findKthLargest(t,s)

    print(r)
    print('---End---')

