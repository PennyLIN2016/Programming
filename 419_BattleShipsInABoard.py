class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        #Runtime: 56 ms, faster than 75.07% of Python online submissions for Battleships in a Board.
        #Memory Usage: 14.9 MB, less than 33.33% of Python online submissions for Battleships in a Board.
        # brutal solution: time:o(n*m) space:o(1)
        if not board or not board[0]: return 0
        res=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i>0 and board[i-1][j]=="X") or (j>0 and board[i][j-1]=="X"):
                    continue
                if board[i][j]=="X":
                    res+=1
        return res




if __name__ == '__main__':
    object = Solution()
    num = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

    print(num)
    print('---Start---')
    r = object.countBattleships(num)
    print(r)
    print('---End---')
