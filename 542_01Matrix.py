class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        #Runtime: 576 ms, faster than 82.25% of Python online submissions for 01 Matrix.
        #Memory Usage: 15.6 MB, less than 18.18% of Python online submissions for 01 Matrix.
        # google solution: bfs+ dp
        if not matrix or not matrix[0]: return matrix
        h,w = len(matrix),len(matrix[0])
        res=[[0]*w for x in range(h)]
        # put all 1 elements in to a queue: bfs
        undoQueue=[(x,y)for x in range(h) for y in range(w) if matrix[x][y]]
        # count the distance
        step=0
        while undoQueue:
            step+=1
            nq,mq=[],[]
            for i,j in undoQueue:
                zero=0
                # for directions
                for dx,dy in zip((1,0,-1,0),(0, 1, 0, -1)):
                    nx,ny=i+dx,j+dy
                    if 0<=nx<h and 0<=ny<w and matrix[nx][ny]==0:
                        zero+=1
                if zero:
                    res[i][j]=step
                    # reachable elements
                    mq.append((i,j))
                else:
                    # unreachable elements
                    nq.append((i,j))
            for i,j in mq:
                matrix[i][j]=0
            undoQueue=nq
        return res
    def updateMatrix1(self, mat: list[list[int]]) -> list[list[int]]:
        # Runtime: 726 ms, faster than 76.94% of Python3 online submissions for 01 Matrix.
        # Memory Usage: 16.8 MB, less than 90.83% of Python3 online submissions for 01 Matrix.
        # BFS solution: time: (m*n*4) = (m*n) space: (m*n) the worse scenario for visit
        m, n = len(mat), len(mat[0])
        dirs = [(-1,0), (1,0), (0, -1), (0,1)]
        visit = collections.deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    visit.append((r, c))
                else:
                    mat[r][c] = float('inf')
        while visit:
            r, c = visit.popleft()
            for x, y in dirs:
                i, j = r + x, c + y
                if 0 <= i < m and 0 <= j < n and mat[i][j] > mat[r][c] + 1:
                    visit.append((i, j))
                    mat[i][j] = mat[r][c] + 1
        return mat

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # 动态规划，从左上角向右下角进行动态规划，再从右小角向左上角动态规划
        # Runtime: 553 ms, faster than 97.61% of Python3 online submissions for 01 Matrix.
        # Memory Usage: 16.5 MB, less than 98.46% of Python3 online submissions for 01 Matrix.
        # dp solution: time: o(n*m) space: o(1)
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    up = mat[r-1][c] if r >0 else float('inf')
                    left = mat[r][c-1] if c > 0 else float('inf')
                    mat[r][c] = min(up + 1, left + 1)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    down = mat[r+1][c] if r < m - 1 else float('inf')
                    right = mat[r][c+1] if c < n-1 else float('inf')
                    mat[r][c] = min(mat[r][c], down + 1, right+ 1)
        return mat
if __name__ == '__main__':
    object = Solution()
    n1=[[0,0,0],
 [0,1,0],
 [0,0,0]]


    print('---Start---')
    print n1
    r = object.updateMatrix(n1)
    print(r)
    print('---End---')
