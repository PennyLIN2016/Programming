class Solution1(object):
    # timeout: 42 / 63 test cases passed.
    # just reuse the implementation of 79_WordSearch
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.exist(board, word):
                res.append(word)
        return res

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

class Solution(object):
    ## Runtime: 834 ms, faster than 95.97% of Python3 online submissions for Word Search II.
    ##Memory Usage: 15.6 MB, less than 70.65% of Python3 online submissions for Word Search II.
    ## trie solution
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]
            word = cur.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                root.pop(letter)

        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
                print('trie: {}'.format(trie))
            cur['#'] = word
        print('all-trie: {}'.format(trie))
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res

obj = Solution()
t1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
t2 = ["oath","pea","eat","rain"]
print(obj.findWords(t1, t2))