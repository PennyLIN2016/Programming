class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 20 ms, faster than 74.68% of Python online submissions for Predict the Winner.
        #Memory Usage: 11.6 MB, less than 100.00% of Python online submissions for Predict the Winner.
        total=sum(nums)
        print total
        self.fD,self.sD={},{}
        one=self.f(nums,0,len(nums)-1)
        print one
        print self.sD
        print self.fD
        return one*2 >=total
    def f(self,nums,start,end):
        # get the nums and get the possible maximum scores
        # for play 2 action
        if start==end:
            return nums[start]
        # in case the combination have been covered from the other direction.
        if(start,end) not in self.fD:
            self.fD[(start,end)]=max(nums[start]+self.s(nums,start+1,end),nums[end]+self.s(nums,start,end-1))
        return self.fD[(start,end)]

    def s(self,nums,start,end):
        # do not get the num and get the possible miximum scores
        # for play2 action
        if start==end:
            return 0
        if(start,end) not in self.sD:
            self.sD[(start,end)]=min(self.f(nums,start+1,end),self.f(nums,start,end-1))
        return self.sD[(start,end)]

    def PredictTheWinner1(self, nums):
        #Runtime: 28 ms, faster than 22.51% of Python online submissions for Predict the Winner.
        #Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Predict the Winner.
        # dynamic programming solution:
        dp = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                dp[j]=max(nums[i]-dp[j],nums[j]-dp[j-1])
        return dp[-1]>=0
    
    
   def PredictTheWinner(self, nums: list[int]) -> bool:
        # Runtime: 147 ms, faster than 20.39% of Python3 online submissions for Predict the Winner.
        # Memory Usage: 13.9 MB, less than 58.68% of Python3 online submissions for Predict the Winner.
        # dp- resursion solution: time: o()
        def dfs(start, end, p1, p2):
            print('start: {} end: {} p1:{} p2:{}'.format(start, end, p1, p2))
            if start > end:
                print('return 1: {}'.format(True if sum(p1) >= sum(p2) else False))
                if sum(p1) > sum(p2):
                    return 1
                elif sum(p1) == sum(p2):
                    return 0
                else:
                    return -1
            p1.append(nums[start])
            res = dfs(start+1, end, p2, p1)
            if res == -1:
                p1.pop()
                print('return 2: True')
                return 1
            elif res == 0:
                p1.pop()
                return 0
            p1.pop()
            print('------1---p1: {} p2: {}'.format(p1, p2))

            p1.append(nums[end])
            res = dfs(start, end-1, p2, p1)
            p1.pop()
            print('return 4: false')
            return res * -1

        player1 = []
        player2 = []
        return dfs(0, len(nums)-1, player1, player2) in [0, 1]

if __name__ == '__main__':
    object = Solution()
    A= [1,3,1]

    print('---Start---')
    r = object.PredictTheWinner(A)
    print(r)
    print('---End---')
