class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Runtime: 16 ms, faster than 95.88% of Python online submissions for Ugly Number.
        # Memory Usage: 11.7 MB, less than 64.23% of Python online submissions for Ugly Number.
        if num<=0: return False
        factor_list = [2,3,5]
        for value in factor_list:
            while num%value==0 and num>=value:
                num/=value
            # no need to continue
            if num==1: break

        return num==1

if __name__ == '__main__':
    s= 320
    p = Solution()
    print(p.isUgly(s))