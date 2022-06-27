class Solution(object):
    def jobScheduling1(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # timeout: 26 / 30 test cases passed.
        # dp solution: time:o(n**2) space: o(n)
        n = len(startTime)
        # sorted by end time
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x:x[1])
        # dp[i] for job i:the best profile
        dp =[0]* (n)
        for i in range(n):
            # get a basic value for this loop
            if i > 0:
                dp[i] = dp[i-1]
            # find the most close job can finished before this job
            for j in range(i-1, -1, -1):
                if jobs[j][1] <= jobs[i][0]:
                    # take this job or not
                    dp[i] = max(dp[i], dp[j] + jobs[i][2])
                    break
            # make sure the first one can get value
            dp[i] = max(dp[i], jobs[i][2])
        return dp[-1]

    def jobScheduling(self, startTime, endTime, profit):
        # Runtime: 645 ms, faster than 72.53% of Python online submissions for Maximum Profit in Job Scheduling.
        # Memory Usage: 27.4 MB, less than 33.52% of Python online submissions for Maximum Profit in Job Scheduling.
        # dp solution: time: o(n* lgn) space: o(n)
        n = len(startTime)
        # sorted by end time
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[1])

        dp = [0] * n
        for i in range(n):
            if i > 0:
                dp[i] = dp[i-1]

            l, r = 0, i
            # binary search for the dp[j]
            while l+1 < r:
                mid = l + (r-l)/2
                if jobs[mid][1] <= jobs[i][0]:
                    l = mid
                else:
                    r = mid
            if jobs[l][1] <= jobs[i][0]:
                dp[i] = max(dp[i], dp[l]+jobs[i][2])

            dp[i] = max(dp[i], jobs[i][2])
        return dp[-1]

obj = Solution()
t1 = [1,2,3,3]
t2 = [3,4,5,6]
t3 = [50,10,40,70]
print(obj.jobScheduling(t1, t2, t3))
