# 47 / 94 test cases passed. time out
# my own solution : time o(4**N) space: o(N)
class Solution1(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if i<0 or j <0 or i >m-1 or j >n-1: return 0
        self.m,self.n,self.d=m,n,N-1
        self.res=0
        self.dfs(i,j,0)
        return self.res

    def dfs(self,r,c,cur):
        if cur>self.d:return
        print ([r,c])
        self.res+= self.newPath(r,c)
        print('cur '+str(cur))
        print('path '+str(self.res))
        if self.res>=10**9+7:
                self.res-=10**9+7
        if r>0: self.dfs(r-1,c,cur+1)
        if r<self.m-1:self.dfs(r+1,c,cur+1)
        if c>0:self.dfs(r,c-1,cur+1)
        if c<self.n-1:self.dfs(r,c+1,cur+1)

    def newPath(self,r,c):
        ans= 0
        if r==0:ans+=1
        if r==self.m-1:ans+=1
        if c==0:ans+=1
        if c==self.n-1:ans+=1
        return ans

class Solution(object):
    def findPaths1(self, m, n, N, i, j):
        # Runtime: 172 ms, faster than 60.29% of Python online submissions for Out of Boundary Paths.
        # Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for Out of Boundary Paths.
        # google solution : dp[d][r][c] from [r,c] path number with d steps(last loop)
        # time o(mnN) space:o(mnN)

        dp=[[[0]*n for _ in range(m)] for _ in range(N+1)]
        for d in range(1,N+1):
            for r in range(m):
                for c in range(n):
                    p1= 1 if r==0 else dp[d-1][r-1][c]
                    p2=1  if r==m-1 else dp[d-1][r+1][c]
                    p3=1 if c==0 else dp[d-1][r][c-1]
                    p4=1 if c==n-1 else dp[d-1][r][c+1]
                dp[d][r][c]=(p1+p2+p3+p4)%(10**9+7)
        return dp[N][i][j]

    def findPaths(self, m, n, N, i, j):
        # Runtime: 132 ms, faster than 79.41% of Python online submissions for Out of Boundary Paths.
        # Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Out of Boundary Paths.
        # improved solution of solution 1 from google:
        # dp solution dp[r][c] currently [r][c]`s path number within d steps
        # time : o(Nmn) space:o(m*n)
        dp= [[0]*n for _ in range(m)]
        for d in range(1,N+1):
            curStatus=[[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    p1 = 1 if r == 0 else dp[r - 1][c]
                    p2 = 1 if r == m - 1 else dp[r + 1][c]
                    p3 = 1 if c == 0 else dp[r][c - 1]
                    p4 = 1 if c == n - 1 else dp[r][c + 1]
                    curStatus[r][c]=(p1+p2+p3+p4)%(10**9+7)
            dp=curStatus
        return dp[i][j]



if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    m = 1
    n = 3
    N = 3
    i = 0
    j = 1


    print('---Start---')
    print (n)
    r = object.findPaths(m,n,N,i,j)
    print(r)
    print('---End---')