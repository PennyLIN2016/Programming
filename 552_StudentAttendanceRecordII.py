class Solution:
    def checkRecord(self, n: int) -> int:
        # "The answer may be very large, so return it modulo 10**9 + 7." -- can't use recursion solution:
        # the stack memory will run out
        # dp solution: time: o(n) space: o(n)
        # Runtime: 1034 ms, faster than 76.01% of Python3 online submissions for Student Attendance Record II.
        # Memory Usage: 17.9 MB, less than 48.07% of Python3 online submissions for Student Attendance Record II.
        if n == 1: return 3
        modu = 1000000007
        # dp[i] the number of all possible attendance(without 'A') with length i
        # end with 'p': dp[i-1] : p can follow any possible attendance
        # end with 'PL': dp[i-2] :
        # end with: 'PLL' + 'PLL': dp[i-3]
        dp = [0] * (n+2)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(2, n+2):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % modu
        res = dp[-1]
        print('dp: {} res: {}'.format(dp, res))
        # the number of all possible attendance (with 'A') records with length n:
        # ∑dp[i+1] *dp[n-i]
        # 'A' can happen once. i+1 = A
        for i in range(n):
            res = (res + dp[i+1] * dp[n-i]) % modu
        return res





if __name__ == '__main__':

    obj = Solution()
    t1 = 5
    print('input: {}'.format(t1))
    r = obj.checkRecord(t1)
    print('output: {}'.format(r))