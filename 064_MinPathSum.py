class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        h = len(grid)
        w = len(grid[0])

        if h == 1:
            return sum(grid[0])
        if w ==1 :
            return sum(grid[:][0])

        path = [0 for i in range(w)]
        path[0] = grid[0][0]
        for p in range(1,w):
            path[p] = path[p-1]+ grid[0][p]

        pre_list = [0 for i in range(h)]
        pre_list[0]= grid[0][0]
        for p in range(1,h):
            pre_list[p] = pre_list[p-1]+ grid[p][0]

        for i in range(1,h):
            pre = pre_list[i]
            for j in range(1,w):
                path[j] = min(pre, path[j]) + grid[i][j]
                pre = path[j]

        return path[-1]






if __name__ == '__main__':

    B = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    #B= [[1]]
    #B= [[0,0],[1,1],[0,0]]
    #B = [[1,0],[0,0]]
    #B = [[1,0]]
    #B = [[1,2],[1,1]]

    A = Solution()
    r = A.minPathSum(B)
    print 'Result:',r





