class Solution(object):
    def findMinDifference1(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        #Runtime: 88 ms, faster than 19.50% of Python online submissions for Minimum Time Difference.
        #Memory Usage: 15 MB, less than 100.00% of Python online submissions for Minimum Time Difference.
        # time : o(nlgn) space o(1)
        def getNum(timeStr):
            return int(timeStr[:2])*60+int(timeStr[3:])
        def getdif(timeStr1,timeStr2):
            time1=getNum(timeStr1)
            time2=getNum(timeStr2)
            return min(time2-time1,1440-(time2-time1))

        timePoints.sort()
        res=getdif(timePoints[0],timePoints[-1])
        for i in range(1,len(timePoints)):
            res= min(getdif(timePoints[i-1],timePoints[i]),res)
        return res

    def findMinDifference(self, timePoints):
        #Runtime: 64 ms, faster than 78.79% of Python online submissions for Minimum Time Difference.
        #Memory Usage: 15.8 MB, less than 100.00% of Python online submissions for Minimum Time Difference.
        # google solution
        def convert(time):
            return int(time[:2])*60 +int(time[3:])
        timePoints=map(convert,timePoints)

        timePoints.sort()
        print timePoints
        print zip(timePoints,timePoints[1:]+timePoints[:1])
        return min((y-x)%(24*60) for x,y in zip(timePoints,timePoints[1:]+timePoints[:1]))









if __name__ == '__main__':
    object = Solution()
    n1=["23:59","00:00"]

    print('---Start---')
    print n1
    r = object.findMinDifference(n1)
    print(r)
    print('---End---')
