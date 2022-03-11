class Solution:
    # the dp[i] is decided by dp[i-1] and dp[i+1], so dp is not workable solution
    def integerReplacement(self, n: int) -> int:
        # Runtime: 32 ms, faster than 85.00% of Python3 online submissions for Integer Replacement.
        # Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Integer Replacement.\
        # bit operation solution: time: o(lgn) space o(1)
        res= 0
        while n>1:
            res += 1
            # n is even
            if n%2 ==0 :
                n>>=1
            # 0b11 and n!= 3
            elif n & 0b10 and n != 3:
                n+=1
            # ob 01 or n=3
            else:
                n-=1
        return res
    def integerReplacement2(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 215 ms, faster than 36.19% of Python online submissions for Integer Replacement.
        #Memory Usage: 13.4 MB, less than 71.43% of Python online submissions for Integer Replacement.
        if n == 1: return 0
        if n%2 == 0:
            return self.integerReplacement(n>>1)+1
        else:
            return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1

if __name__ == '__main__':

    s= 1234
    p = Solution()
    print(p.integerReplacement(s))
