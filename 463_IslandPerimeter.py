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

if __name__ == '__main__':
    object = Solution()
    A=  [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print('---Start---')
    r = object.islandPerimeter(A)
    print(r)
    print('---End---')
