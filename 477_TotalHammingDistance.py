class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 372 ms, faster than 79.60% of Python online submissions for Total Hamming Distance.
        #Memory Usage: 12.8 MB, less than 50.00% of Python online submissions for Total Hamming Distance.
        res=0
        for i in range(32):
            # for each bit
            count=0
            for v in nums:
                count+= (v>>i)&1
            # the count in this bit: multiplication of  the 1 nubmers and  0 numbers
            res+= count*(len(nums)-count)
        return res


if __name__ == '__main__':
    object = Solution()
    A= [4,14,2]

    print('---Start---')
    r = object.totalHammingDistance(A)
    print(r)
    print('---End---')
