import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        #Runtime: 188 ms, faster than 65.08% of Python online submissions for Target Sum.
        #Memory Usage: 12.2 MB, less than 42.86% of Python online submissions for Target Sum.
        # DP solution: time o(n)
        # make sure dp[i] points to different object.
        dp=[collections.defaultdict(int) for _ in range(len(nums)+1)]
        # d[i] is dict{key : value} key:sum of 0~i  value : the number of combination to get the sum
        dp[0][0]=1
        for i,value in enumerate(nums):
            for s,count in dp[i].items():
                dp[i+1][s+value]+=count
                dp[i+1][s-value]+=count
        return dp[-1][S]


if __name__ == '__main__':
    object = Solution()
    A=  [1, 1, 1, 1, 1]
    b= 3

    print('---Start---')
    r = object.findTargetSumWays(A,b)
    print(r)
    print('---End---')
