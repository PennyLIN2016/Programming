class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Runtime: 406 ms, faster than 49.07% of Python online submissions for Number of Islands.
        # Memory Usage: 28.6 MB, less than 86.08% of Python online submissions for Number of Islands.
        # dfs solution: time: o(m*n): the number for dfs is the number of island. 
        # space: o(1):ignore the stack space for dfs
        def dfs(r, c):
            dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for v in dirs:
                x, y = r + v[0], c + v[1]
                #print('x: {} y: {}'.format(x, y))
                if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1 or grid[x][y] == '0':
                    continue
                grid[x][y] = '0'
                dfs(x, y)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                grid[i][j] = '0'
                res += 1
                dfs(i, j)
                #print('i: {} j: {} grid: {}'.format(i, j, grid))
        return res



obj = Solution()
t1 =  [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(obj.numIslands(t1))