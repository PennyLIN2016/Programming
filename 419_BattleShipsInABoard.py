class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Runtime: 112 ms, faster than 14.51% of Python online submissions for Battleships in a Board.
        # Memory Usage: 16.8 MB, less than 70.47% of Python online submissions for Battleships in a Board.
        # brutal solution
        # time: o(m*n) o(m*n)
        m, n= len(board), len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                # Only two directions: just count the first 'X'
                if (i> 0 and board[i-1][j] == 'X') or(j>0 and board[i][j-1]== 'X'):
                    continue
                # new ship
                if board[i][j] == 'X':
                    res += 1
        return res



if __name__ == '__main__':
    object = Solution()
    num = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

    print(num)
    print('---Start---')
    r = object.countBattleships(num)
    print(r)
    print('---End---')
