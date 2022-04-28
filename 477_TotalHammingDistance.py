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
    def totalHammingDistance1(self, nums: list[int]) -> int:
        # Time Limit Exceeded: 35 / 46 test cases passed.
        # force solution: time: o(n**2) space: o(1)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] != nums[j]:
                    res += self.hammingDistance(nums[i], nums[j])
        return res

    def hammingDistance(self, n1, n2):
        #print('n1: {} n2: {} dis: {}'.format(n1, n2, str(bin(n1 ^ n2))))
        return (str(bin(n1 ^ n2))).count('1')

    def totalHammingDistance(self, nums: list[int]) -> int:
        # Runtime: 695 ms, faster than 46.78% of Python3 online submissions for Total Hamming Distance.
        # Memory Usage: 15.6 MB, less than 28.07% of Python3 online submissions for Total Hamming Distance.
        # frequency logical solution: time: o(32* n) = o(n) space: o(1)
        res = 0
        # find 1  number and 0 number in i bit
        # the differece sum in i bit:  the combination of (1, 0) = ones * zeros
        for i in range(32):
            ones = 0
            for v in nums:
                # &1 : just get the most left bit
                ones += (v >> i) & 1
            res += ones * (len(nums)-ones)
        return res

if __name__ == '__main__':
    object = Solution()
    A= [4,14,2]

    print('---Start---')
    r = object.totalHammingDistance(A)
    print(r)
    print('---End---')
