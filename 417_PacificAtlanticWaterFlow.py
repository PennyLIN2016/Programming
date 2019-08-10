class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        #Runtime: 268 ms, faster than 73.93% of Python online submissions for Pacific Atlantic Water Flow.
        #Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Pacific Atlantic Water Flow.
        # dfs solution(from other website)
        if not matrix or not matrix[0]: return []
        m,n = len(matrix),len(matrix[0])
        # the water visitable matrix for pacific and atlantic
        p=[[0]*n for _ in range(m)]
        a=[[0]*n for _ in range(m)]
        # set the target points of counting
        for i in range(m):
            self.dfs(p,matrix,m,n,i,0)
            self.dfs(a,matrix,m,n,i,n-1)
        for j in range(n):
            self.dfs(p,matrix,m,n,0,j)
            self.dfs(a,matrix,m,n,m-1,j)
        res=[]
        for i in range(m):
            for j in range(n):
                if p[i][j] and a[i][j]:
                    res.append([i,j])
        return res
    def dfs(self,v,matrix,m,n,i,j):
        # each input(i,j) should have been visitable
        # i,j is the target point in this invoking
        v[i][j]=1
        direct=[(-1,0),(1,0),(0,1),(0,-1)]
        for d in direct:
            # set the direction of the water
            x,y = i+d[0],j+d[1]
            # if skip the traveled (x,y)
            # the hight of (x,y) should >=(i,j) the water can flow to the target
            if x<0 or x>=m or y<0 or y>=n or v[x][y] or matrix[x][y]<matrix[i][j]:
                continue
            self.dfs(v,matrix,m,n,x,y)


if __name__ == '__main__':
    object = Solution()
    num = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    #num=[[1,1],[1,1],[1,1]]
    print(num)
    print('---Start---')
    r = object.pacificAtlantic(num)
    print(r)
    print('---End---')
