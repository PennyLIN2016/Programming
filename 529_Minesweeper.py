class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        #Runtime: 168 ms, faster than 55.25% of Python online submissions for Minesweeper.
        #Memory Usage: 14.2 MB, less than 42.86% of Python online submissions for Minesweeper.
        # google solution : time o(m*n) space :o(1)
        if not board or not click: return []
        row ,col = click[0],click[1]
        if board[row][col]=='M':
            board[row][col]='X'
        else:
            # get the digital number:1~8
            count=0
            for i in range(-1,2):
                for j in range(-1,2):
                    # the 8 neighbour position
                    if i==0 and j==0:
                        # the click position
                        continue
                    r,c= row+i, col+j
                    if not (0<=r <len(board)) or not (0<=c<len(len[r])):
                        # invalid position
                        continue
                    if board[r][c]=='M' or board[r][c]=='X':
                        count+=1
        if count:
            board[row][col]=chr(count+ord('0'))
        else:
            board[row][col]='B'
            for i in xrange(-1,2):
                for j in xrange(-1,2):
                    
                    
                    if i==0 and j==0:
                        continue
                    r,c = row+i,col+j
                    if not (0<=r <len(board)) or not (0<=c<len(len[r])):
                        continue
                    if board[r][c]=='E':
                        self.updateBoard(board,(r,c))
        return board
class Solution:
    # Runtime: 312 ms, faster than 21.14% of Python3 online submissions for Minesweeper.
    # Memory Usage: 17 MB, less than 35.84% of Python3 online submissions for Minesweeper.
    # time: O(n*m) space: o(1)
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        def clickBoard(pos):
            x, y = pos[0], pos[1]
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            if board[x][y] in visited:
                return
            cur = 0
            for v in dirs:
                x1, y1 = x + v[0], y + v[1]
                if not(0 <= x1 < len(board)) or not(0 <= y1 < len(board[0])):
                    continue
                if board[x1][y1] == 'M':
                    cur += 1
            board[x][y] = str(cur) if cur != 0 else 'B'
            if cur > 0:
                return
            for v2 in dirs:
                x2, y2 = x + v2[0], y + v2[1]
                if 0 <= x2 < len(board) and 0 <= y2 < len(board[0]):
                    clickBoard([x2,y2])

        dirs = [[-1,-1] ,[-1,0], [-1,1], [0,-1], [0,1], [1,-1],[1,0],[1,1]]
        visited = set([str(i) for i in range(1, 9)])
        visited.add('B')
        clickBoard(click)
        return board


if __name__ == '__main__':
    object = Solution()
    s = [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
      ['E', 'E', 'E', 'E', 'E'],
      ['E', 'E', 'E', 'E', 'E']]

    Click =[3,0]


    print('---Start---')
    print s
    r = object.updateBoard(s)
    print(r)
    print('---End---')
