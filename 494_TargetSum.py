import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # can't pass on 4/05/2022
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
    
    def findTargetSumWays1(self, nums: list[int], target: int) -> int:
        # 61 / 139 test cases passed.
        # timeout at [42, 16, 31, 11, 36, 19, 9, 3, 25, 0, 27, 29, 35, 29, 45, 15, 35, 42, 35, 23]: the answer is corrct
        # basically, if the response is the number , not the combinations, the dfs solution would be timeout
        # have to use dp solution with time: o(n)

        def dfs(index, aim):
            print('index: {} aim: {}'.format(index, aim))
            if index == l:
                if aim == 0:
                    res[0] += 1
                    print('---res+1')
                return
            dfs(index+1, aim - nums[index])
            dfs(index+1, aim + nums[index])

        l = len(nums)
        res = [0]
        dfs(0, target)
        return res[0]

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # Runtime: 150 ms, faster than 94.03% of Python3 online submissions for Target Sum.
        # Memory Usage: 14 MB, less than 93.24% of Python3 online submissions for Target Sum.
        # math+ dp solution: time: o(target*n) space: o(target*n)
        # math: sum(positive) + sum(negative) = target --> 2* sum(positive) = target + sum(nums)
        #--> sum(positive) = (target + sum) //2
        # the dp is just to find a "+" combination to target for (target + sum) //2, donot need to care about
        # the "-" numbers

        numSum = sum(nums)
        # no such combination
        if (target + numSum) % 2 == 1:
            return 0
        aim = (target + numSum) // 2
        # the "+" combination should be positive as well
        if aim < 0 : return 0
        # the dp stores the number of ways to get target to i
        dp = [0] * (aim + 1)
        # all numbers to be "-"
        dp[0] = 1
        for v in nums:
            i = aim
            # fresh the dp greater than v
            # the loop is to take v at least.
            # make sure the loop used the last loop result 
            # have to travel from aim to v
            while(i >= v):
                dp[i] += dp[i-v]
                i -= 1

        return dp[aim]

if __name__ == '__main__':
    object = Solution()
    A=  [1, 1, 1, 1, 1]
    b= 3

    print('---Start---')
    r = object.findTargetSumWays(A,b)
    print(r)
    print('---End---')
