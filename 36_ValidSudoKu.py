class Solution:
    def isValidSudoku1(self, board: list[list[str]]) -> bool:
        # force solution: time: o(row*col) space: O(1)

        """
        # solution 1a
        #Runtime: 131 ms, faster than 57.99% of Python3 online submissions for Valid Sudoku.
        #Memory Usage: 13.9 MB, less than 81.72% of Python3 online submissions for Valid Sudoku.
        rowVisited = [set() for _ in range(9)]
        colVisited = [set() for _ in range(9)]
        squareVisited = [set() for _ in range(9)]
        """
        # solution 1b
        # Runtime: 151 ms, faster than 40.96% of Python3 online submissions for Valid Sudoku.
        # Memory Usage: 14 MB, less than 34.33% of Python3 online submissions for Valid Sudoku.
        import collections
        rowVisited = collections.defaultdict(lambda: set())
        colVisited = collections.defaultdict(lambda: set())
        squareVisited = collections.defaultdict(lambda: set())

        for r in range(9):
            for c in range(9):
                print('r: {} c: {} board[r][c]: {}'.format(r, c, board[r][c]))
                if board[r][c] == '.':
                    continue

                if board[r][c] in rowVisited[r]:
                    return False
                else:
                    rowVisited[r].add(board[r][c])

                if board[r][c] in colVisited[c]:
                    return False
                else:
                    colVisited[c].add(board[r][c])

                index = int(c / 3) * 3 + int(r / 3)
                print('index: {}'.format(index))
                if board[r][c] in squareVisited[index]:
                    return False
                else:
                    squareVisited[index].add(board[r][c])
                print('rowVisited:{} \ncolVisited: {} \nsquareVisited: {}'.format(rowVisited, colVisited, squareVisited))
        return True


if __name__ == '__main__':
    obj = Solution()
    t1 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print('input: {}'.format(t1))
    r = obj.isValidSudoku(t1)
    print('output: {}'.format(r))
    print('--------END--------')