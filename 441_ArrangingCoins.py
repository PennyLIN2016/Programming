class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brutal solution :
        # Runtime: 637 ms, faster than 42.75% of Python online submissions for Arranging Coins.
        # Memory Usage: 13.5 MB, less than 32.43% of Python online submissions for Arranging Coins.

        res = 0
        while n >= res + 1:
            res += 1
            n -= res
        return res
    def arrangeCoins1(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 95.71% of Python online submissions for Arranging Coins.
        #Memory Usage: 11.9 MB, less than 14.29% of Python online submissions for Arranging Coins.
        # math solution: time:o(1) space:o(1)
        import math
        k=int(math.sqrt(2*n))
        return  k-1 if k*(k+1)>2*n else k


if __name__ == '__main__':
    object = Solution()
    num =  789796585
    #num="abab"
    #p="ab"

    print(num)
    print('---Start---')
    r = object.arrangeCoins(num)
    print(r)
    print('---End---')
