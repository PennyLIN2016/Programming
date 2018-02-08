
class question(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, dp):
            for i in xrange(2, n):
                if dp[i] == 1:
                    k = i * i
                    if k >= n:
                        return
                    while k < n:
                        dp[k] = 0
                        k += i
        if n < 2:
            return 0
        ans = 0
        dp = [1] * n
        dp[0] = 0
        dp[1] = 0
        helper(n, dp)

        return sum(dp)


if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs.strip()
    #r = k.LongestPaliSubstring(inputs.strip())
    r = k.countPrimes(int(inputs))
    print  '1-Result : ',r




