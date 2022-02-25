class Solution(object):
    def isPowerOfFour1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Runtime: 24 ms, faster than 65.50% of Python online submissions for Power of Four.
        #Memory Usage: 11.9 MB, less than 7.37% of Python online submissions for Power of Four.
        # space o(1) time (n/4) but use loop
        if num<=0 : return False
        while num>1:
            if num%4 != 0 :return False
            num>>=2
        return True

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ##Runtime: 20 ms, faster than 79.42% of Python online submissions for Power of Four.
        #Memory Usage: 11.9 MB, less than 13.86% of Python online submissions for Power of Four.
        # no loop solution time: o(1) space: o(1)
        # num&(num-1)==0: 2**x -- only the most right bit is 1
        # num&(0x55555555)!=0 at least one odd bit is 1. 0x55555555= 10101010101010101
        return num>0 and (num&(num-1)==0)and(num&(0x55555555)!=0)


if __name__ == '__main__':
    k = Solution()
    l= 16

    r = k.isPowerOfFour(l)
    print(r)
    print('---End---')



