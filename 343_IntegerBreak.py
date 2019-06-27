class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 91.04% of Python online submissions for Integer Break.
        #Memory Usage: 11.8 MB, less than 41.56% of Python online submissions for Integer Break.
        # time : o(n) space: o(1)
        # n=4 --1*3 or 2*2
        # n=5-- 2*3
        if n==2 :return 1
        if n==3 : return 2
        res=1
        while n>4:
            res*=3
            n-=3
        return res*n


if __name__ == '__main__':
    k = Solution()
    l= 10

    r = k.integerBreak(l)
    print(r)
    print('---End---')



