class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        h = len(obstacleGrid)
        w = len(obstacleGrid[0])

        if obstacleGrid[h-1][w-1] == 1:
            return 0

        path = [0 for i in range(w)]
        for p in range(w):
            if obstacleGrid[0][p]==1:
                break
            path[p]=1

        pre_list = [0 for i in range(h)]
        for p in range(h):
            if obstacleGrid[p][0]==1:
                break
            pre_list[p]= 1

        for i in range(1,h):
            pre= pre_list[i]
            for j in range(1,w):
                if obstacleGrid[i][j-1] == 1:
                    pre = 0
                if  obstacleGrid[i-1][j] == 1:
                    path[j] = pre
                else:
                    path[j] = pre + path[j]
                pre = path[j]
        return path[-1]

if __name__ == '__main__':

    '''B = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
        ]'''
    #B= [[1]]
    #B= [[0,0],[1,1],[0,0]]
    #B = [[1,0],[0,0]]
    B = [[1,0]]

    A = Solution()
    r = A.uniquePathsWithObstacles(B)
    print 'Result:',r





