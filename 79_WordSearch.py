class Solution(object):
    ## Runtime: 8208 ms, faster than 27.28% of Python online submissions for Word Search.
    # Memory Usage: 13.4 MB, less than 66.53% of Python online submissions for Word Search.
    # DFS solution: time: O(n*m)
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if self.dfs(board, i, j, word, 0, visited):
                        return True
                    visited.remove((i, j))
        return False

    def dfs(self, board, r, c, word, index, used):
        if index == len(word) - 1:
            print('used: {}'.format(used))
            return True
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        print('r: {} c: {} value: {}'.format(r, c, board[r][c]))
        for v in dirs:
            x, y = r + v[0], c + v[1]
            print('x: {} y: {} used: {}'.format(x, y, used))
            if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0])-1 or (x, y) in used:
                continue
            if board[x][y] == word[index+1]:
                used.add((x, y))
                if self.dfs(board, x, y, word, index+1, used):
                    return True
                used.remove((x, y))
        return False


obj = Solution()
t1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
t2 = "ABCB"
print(obj.exist(t1, t2))