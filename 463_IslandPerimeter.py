class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Runtime: 424 ms, faster than 95.84% of Python online submissions for Island Perimeter.
        #Memory Usage: 12 MB, less than 82.35% of Python online submissions for Island Perimeter.
        #time o(h*w) space:o(1)
        h=len(grid)
        w= len(grid[0]) if h else 0
        res=0
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    res+=4
                    if i>0 and grid[i-1][j]:
                        res-=2
                    if j>0 and grid[i][j-1]:
                        res-=2
        return res
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Runtime: 467 ms, faster than 72.73% of Python online submissions for Island Perimeter.
        # Memory Usage: 13.9 MB, less than 33.40% of Python online submissions for Island Perimeter.
        # brutal solution time: o(n*m) space: o(1)
        res = 0
        row, col = len(grid), len(grid[0])
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                for v in dir:
                    rr, cc = r + v[0], c + v[1]
                    if rr < 0 or rr > row-1 or cc < 0 or cc > col-1 or grid[rr][cc] == 0:
                        res += 1
        return res
    

if __name__ == '__main__':
    object = Solution()
    A=  [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print('---Start---')
    r = object.islandPerimeter(A)
    print(r)
    print('---End---')
