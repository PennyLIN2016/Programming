class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        # Runtime: 2244 ms, faster than 58.33% of Python online submissions for Find Players With Zero or One Losses.
        # Memory Usage: 74.1 MB, less than 48.61% of Python online submissions for Find Players With Zero or One Losses.
        # hashmap solution: time: o(nlgn) space: o(n)
        plays = {}
        for v in matches:
            winner, loser = v[0], v[1]
            if winner not in plays:
                plays[winner] = 0
            if loser not in plays:
                plays[loser] = 1
            else:
                plays[loser] += 1
        print(plays)
        r1 = []
        r2 = []
        for k in plays:
            if plays[k] == 0:
                r1.append(k)
            elif plays[k] == 1:
                r2.append(k)
        r1.sort()
        r2.sort()
        return [r1, r2]

obj = Solution()
t1 = [[2,3],[1,3],[5,4],[6,4]]
print(obj.findWinners(t1))
