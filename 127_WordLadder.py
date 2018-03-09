
from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def get_path(beginWord,endWord,unvisited):
            r = []
            for c in 'abcdefghigklmnopqrstuvwxyz':
                for j in xrange(len(beginWord)):
                    tmp = beginWord[:j]+c+beginWord[j+1:]
                    if tmp == beginWord:
                        continue
                    if tmp in unvisited:
                        yield tmp


        unvisited = set(wordList)
        queue = deque([beginWord])
        length = 0
        while queue:
            length += 1
            for i in xrange(len(queue)):
                next = queue.popleft()
                for val in get_path(next,endWord,unvisited):
                    if val == endWord:
                        return length+1
                    queue.append(val)
                    unvisited.remove(val)
        return 0


if __name__ == '__main__':

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    k = Solution()
    r = k.ladderLength(beginWord, endWord, wordList)

    print r
