class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #Runtime: 24 ms, faster than 57.51% of Python online submissions for Game of Life.
        #Memory Usage: 11.8 MB, less than 47.05% of Python online submissions for Game of Life.
        # time O(m*n) space: constant
        if not board or not board[0]: return board
        m =len(board)
        n= len(board[0])
        for i in range(m):
            for j in range(n):
                l = max(0,i-1)
                r= min(m-1,i+1)
                u=max(0,j-1)
                d= min(n-1,j+1)
                sum_live= -board[i][j]
                #board[i][j] 0->0 :0 /0->1:3/1->1:1/1->0:2
                for k in range(l,r+1):
                    for t in range(u,d+1):
                        if board[k][t]==1 or board[k][t]==2:
                            sum_live+=1
                if board[i][j]==1 and (sum_live<2 or sum_live>3):
                    board[i][j]=2
                elif board[i][j]==0 and (sum_live==3):
                    board[i][j]=3
        for i in range(m):
            for j in range(n):
                if board[i][j]==0 or board[i][j]==2:
                    board[i][j]= 0
                else:
                    board[i][j]=1
        return board










if __name__ == '__main__':
    s=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
    ]
    object = Solution()
    r = object.gameOfLife(s)

    print(r)
    print('---End---')



