class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Runtime: 65 ms, faster than 56.30% of Python online submissions for Shortest Word Distance.
        # Memory Usage: 18.3 MB, less than 18.77% of Python online submissions for Shortest Word Distance.
        # time: o(n) space: o(1)
        p1, p2 = float('-inf'), float('-inf')
        minDist = float('inf')
        for i, v in enumerate(wordsDict):
            print('v: {} p1: {} p2: {}'.format(v, p1, p2))
            if v == word1:
                p1 = i
                minDist = min(minDist, p1-p2)
            elif v == word2:
                p2 = i
                minDist = min(minDist, p2-p1)
            print('minDist: {} p1: {} p2: {}'.format(minDist, p1, p2))
        return minDist

obj = Solution()
t1 = ["practice", "makes", "perfect", "coding", "makes"]

t3 = "makes"
t2 = "coding"
print(t1)
print(obj.shortestDistance(t1, t2, t3))
