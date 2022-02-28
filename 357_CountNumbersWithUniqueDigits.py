class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 4 ms, faster than 100.00% of Python online submissions for Count Numbers with Unique Digits.
        #Memory Usage: 11.9 MB, less than 11.54% of Python online submissions for Count Numbers with Unique Digits.
        # time: o(n), space:o(n)
        # the possible unique digit in the bit
        factor= [9,9,8,7,6,5,4,3,2,1]
        # pre: the previous unique digits number
        res,pre= 1,1
        # if n>10, the res should be the same to 10
        for i in range(min(n,10)):
            pre*=factor[i]
            res+=pre
        return res

    def countNumbersWithUniqueDigits2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]* (n+1)
        for i in range(1, n+1):
            if i == 1:
                pre = 9
            elif i == 2:
                pre = 81
            else:
                pre *= (11-i)

            # pre  the count of i-digit number without repeated digit.
            # 0 - 1
            # 1- 10
            # 2- 9*9
            dp[i] = dp[i-1] + pre

        return dp[n]

if __name__ == '__main__':
    k = Solution()
    n1 = 10

    r = k.countNumbersWithUniqueDigits(n1)
    print(r)
    print('---End---')
