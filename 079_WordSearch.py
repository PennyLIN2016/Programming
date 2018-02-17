class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word =='':
            return True
        if len(board)== 0:
            return False

        visited = [[0]*len(board[0]) for i in xrange(len(board))]
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        def find_word(i,j,board,visited,word,index):
            if word[index]!= board[i][j]:
                return False
            if len(word)-1 == index:
                return True
            for direction in dir:
                ni, nj = i+direction[0],j+direction[1]
                if ni>= 0 and ni< len(board) and nj >= 0 and nj < len(board[0]):
                    if visited[ni][nj]== 0:
                        visited[ni][nj]= 1
                        if find_word(ni,nj,board,visited,word,index+1):
                            return True
                        visited[ni][nj]= 0
            return False

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                visited[i][j]= 1
                if find_word(i,j,board,visited,word,0):
                    return True
                visited[i][j]= 0
        return False


if __name__ == '__main__':

    M = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
    w = 'ABCCED'

    A = Solution()
    r = A.exist(M,w)
    print 'Result:',r





