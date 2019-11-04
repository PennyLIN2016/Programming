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
