class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 216 ms, faster than 98.21% of Python online submissions for Minimum Moves to Equal Array Elements.
        #Memory Usage: 12.9 MB, less than 50.00% of Python online submissions for Minimum Moves to Equal Array Elements.
        # to increase n-1 elements by 1 equals to decease the left one element by 1.
        # the time is the gaps for minimum element to others respectively.
        return sum(nums)-min(nums)*len(nums)



if __name__ == '__main__':
    object = Solution()
    num =  [1,2,3]

    print(num)
    print('---Start---')
    r = object.minMoves(num)
    print(r)
    print('---End---')
