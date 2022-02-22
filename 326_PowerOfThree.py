class Solution(object):
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ##Runtime: 60 ms, faster than 93.67% of Python online submissions for Power of Three.
        #Memory Usage: 11.7 MB, less than 54.75% of Python online submissions for Power of Three.
        #brutal solution time: o(n/3) space: o(1)
        if n<1: return False
        while n!=1:
            if (n%3!=0):
                return False
            n/=3
        return True
    
    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # brutal solution:
        #Runtime: 76 ms, faster than 84.30% of Python online submissions for Power of Three.
        #Memory Usage: 13.5 MB, less than 19.93% of Python online submissions for Power of Three.
        # time: o(nlog3) space :o(1)
        if n == 0: return False
        if n == 1: return True
        i = 1
        while i < n:
            i *= 3
            if i == n: return True

        return False

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Runtime: 72 ms, faster than 82.00% of Python online submissions for Power of Three.
        #Memory Usage: 11.7 MB, less than 68.66% of Python online submissions for Power of Three
        #brutal solution time: o(n/3) space: o(1)   : math.log(243,3)=4.999999999999999 so int() can not work in some case.
        # round should be good.
        import math
        return n>0 and 3**round(math.log(n,3))==n

if __name__ == '__main__':
    k = Solution()
    j = 243

    r = k.isPowerOfThree(j)

    print(r)
    print('---End---')



