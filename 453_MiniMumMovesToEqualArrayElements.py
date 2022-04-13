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
    
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 209 ms, faster than 92.06% of Python online submissions for Minimum Moves to Equal Array Elements.
        # Memory Usage: 14.7 MB, less than 39.68% of Python online submissions for Minimum Moves to Equal Array Elements.
        # Time :o(n) space: o(1)
        # "In one move, you can increment n - 1 elements of the array by 1" equals to one element decrease by 1
        # So the solution is the sum of all element gap to the minimum value
        minValue = min(nums)
        res = 0
        for v in nums:
            res += v - minValue
        return res



if __name__ == '__main__':
    object = Solution()
    num =  [1,2,3]

    print(num)
    print('---Start---')
    r = object.minMoves(num)
    print(r)
    print('---End---')
