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
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 29 ms, faster than 63.33% of Python online submissions for Arithmetic Slices.
        #Memory Usage: 13.6 MB, less than 59.45% of Python online submissions for Arithmetic Slices.
        # time: o(n) space: o(1)
        if len(nums)<3: return 0
        step = nums[1]-nums[0]
        res, count = 0, 2
        for i in range(2, len(nums)):
            if nums[i]- nums[i-1] == step:
                count += 1
            else:
                # math: sum[1:n] = n*(n-1)/2
                res += (count-1)*(count-2)/2
                step = nums[i]- nums[i-1]
                count = 2
        #print('count: {}'.format(count))
        return res + (count-1)*(count-2)/2
  def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        t = 1
        for i in range(2, len(A)):
            # the nth arithmetic num can add n-2 matches
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                res += t
                t += 1
            else:
                t = 1
        return res


if __name__ == '__main__':
    object = Solution()
    num = [1, 2, 3, 4,5]

    print(num)
    r = object.numberOfArithmeticSlices(num)
    print(r)
    print('---End---')
