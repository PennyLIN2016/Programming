class Solution(object):
    # passed 20.50%
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        i_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='1':
                    i_count += 1
                    self.expand_island(grid,i,j)

        return i_count

    def expand_island(self,grid,i,j):
        grid[i][j] = "0"
        if i > 0  and grid[i-1][j] == "1":
            grid[i - 1][j] == "0"
            self.expand_island(grid,i-1,j)
        if i < len(grid)-1 and grid[i+1][j] == "1":
            grid[i + 1][j] == "0"
            self.expand_island(grid,i+1,j)
        if j > 0 and grid[i][j-1] == "1":
            grid[i][j-1] == "0"
            self.expand_island(grid,i,j-1)
        if j < len(grid[i])-1 and grid[i][j + 1] == "1":
            grid[i][j + 1] == "0"
            self.expand_island(grid, i, j +1)
        return


if __name__ == '__main__':
    """A = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
    ]

    A = [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]]"""
    A = [["1","1","1"],
         ["0","1","0"],
         ["1","1","1"]]

    t = Solution()
    print(t.numIslands(A))