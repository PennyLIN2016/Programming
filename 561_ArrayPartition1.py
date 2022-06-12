class Solution(object):
    def arrayPairSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 264 ms, faster than 47.51% of Python online submissions for Array Partition I.
        #Memory Usage: 14.2 MB, less than 6.06% of Python online submissions for Array Partition I.
        # my own solution: time : o(nlgn) space : o(1)
        nums.sort()
        res=0
        for i in range(0,len(nums),2):
            res+=nums[i]
        return res

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 244 ms, faster than 97.95% of Python online submissions for Array Partition I.
        #Memory Usage: 14 MB, less than 69.70% of Python online submissions for Array Partition I.
        # the same thought to the solution 1: simple syntax more efficient.
        nums.sort()
        # efficent solution
        return sum(nums[::2])

if __name__ == '__main__':
    object = Solution()
    n1=[1,4,3,2]


    print('---Start---')

    r = object.arrayPairSum(n1)
    print(r)
    print('---End---')
