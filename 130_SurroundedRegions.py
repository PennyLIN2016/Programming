from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)== 0:
            return
        ## the not closed 'O ' changed to 'k'
        h = len(board)
        w = len(board[0])
        # Check the outside circle.
        s = deque()
        for i in xrange(h):
            if board[i][0]== 'O':
                board[i][0] = 'K'
                s.append([i,0])
            if board[i][w-1]== 'O':
                board[i][w-1] = 'K'
                s.append([i,w-1])
        for j in xrange(w):
            if board[0][j]== 'O':
                board[0][j] = 'K'
                s.append([0,j])
            if board[h-1][j]== 'O':
                board[h-1][j] = 'K'
                s.append([h-1,j])
        while s:
            tmp = s.pop()
            y = tmp[0]
            x = tmp[1]
            if y > 1 and board[y-1][x] == 'O':
                board[y-1][x] = 'K'
                s.append([y-1,x])
            if x>1 and board[y][x-1] == 'O':
                board[y][x-1]= 'K'
                s.append([y,x-1])
            if y < h-1 and board[y+1][x] == 'O':
                board[y+1][x] = 'K'
                s.append([y+1,x])
            if x< w-1 and board[y][x+1] == 'O':
                board[y][x+1]= 'K'
                s.append([y,x+1])

        # replace 'k' to 'O' and others replace to 'X'
        for j in xrange(len(board)):
            for i in xrange(len(board[0])):
                if board[j][i]== 'K':
                    board[j][i] ='O'
                else:
                    board[j][i] ='X'



if __name__ == '__main__':

    '''A = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X'],
        ]'''
    A = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]




    k = Solution()
    print A
    k.solve(A)

    print A
