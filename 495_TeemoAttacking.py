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
    
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        # Runtime: 382 ms, faster than 37.47% of Python3 online submissions for Teemo Attacking.
        # Memory Usage: 15.6 MB, less than 12.23% of Python3 online submissions for Teemo Attacking.
        # brutal solution: time: o(n) space: o(1)
        if duration == 0:
            return 0
        res = 0
        # v can be 0
        end = -1
        for v in timeSeries:
            print('before: res: {} end: {} v:{}'.format(res, end, v))
            if v > end:
                res += duration
            else:
                res += duration - (end - v + 1)
            end = v + duration - 1
            print('after: res: {} end: {}'.format(res, end))
        return res


if __name__ == '__main__':
    object = Solution()
    A=  [1,4]
    b= 2

    print('---Start---')
    r = object.findPoisonedDuration(A,b)
    print(r)
    print('---End---')
