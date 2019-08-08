class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #Runtime: 20 ms, faster than 90.30% of Python online submissions for Arithmetic Slices.
        #Memory Usage: 12.1 MB, less than 85.71% of Python online submissions for Arithmetic Slices.
        # dp solution: time : o(n) time: o(n)
        if not A or len(A)<3:return 0
        dp=[0]* len(A)
        for i in range(1,len(A)-1):
            # dp[i]: including A[i+1],the numberOf ArithmeticSlices
            # if the A[i+1] keep the previous step, the dp[i] should be dp[i-1]+1
            if A[i]-A[i-1]==A[i+1]-A[i]:
                dp[i]=dp[i-1]+1
        return sum(dp)

if __name__ == '__main__':
    object = Solution()
    num = [1, 2, 3, 4,5]

    print(num)
    r = object.numberOfArithmeticSlices(num)
    print(r)
    print('---End---')
