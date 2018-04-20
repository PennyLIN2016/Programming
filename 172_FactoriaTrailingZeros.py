class Solution(object):
    # a good solution
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        # the numbers of  factor of 5,25,125.....
        while n >= 5:
            n = int(n/5)
            r += n
        return r

if __name__ == '__main__':

    s = 30

    k = Solution()

    print (k.trailingZeroes(s))