class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        #Runtime: 220 ms, faster than 94.84% of Python online submissions for Teemo Attacking.
        #Memory Usage: 12.8 MB, less than 50.00% of Python online submissions for Teemo Attacking.
        # time : o(n) space:o(1)
        res=0
        pre= -duration
        for value in timeSeries:
            if value-pre>=duration:
                res+=duration
            else:
                res+=value-pre
            pre=value
        return res


if __name__ == '__main__':
    object = Solution()
    A=  [1,4]
    b= 2

    print('---Start---')
    r = object.findPoisonedDuration(A,b)
    print(r)
    print('---End---')
