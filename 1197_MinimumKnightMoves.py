class Solution(object):
    def minKnightMoves1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # the solution is Memory Limit Exceeded
        # bfs solution:
        if x == 0 and y == 0:
            return 0

        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1,), (-1, 2)]
        stack = [(0, 0)]
        visited = set()
        l = 0
        while stack:
            l += 1
            tmp = []
            for v in stack:
                for d in dirs:
                    xx, yy = v[0] + d[0], v[1] + d[1]
                    if xx == x and yy == y:
                        return l
                    if (xx, yy) not in visited:
                        tmp.append((xx, yy))
            stack = tmp


    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #Runtime: 2300 ms, faster than 59.87% of Python online submissions for Minimum Knight Moves.
        # Memory Usage: 22.6 MB, less than 54.61% of Python online submissions for Minimum Knight Moves.
        # bfs+ deque solution time: o(m*n) the board size space: o(m*n)
        # this solution should set the range of the board.

        import collections
        # the board is symmetric: minimize the range
        x, y = abs(x), abs(y)
        if x == 0 and y == 0: return 0
        # this position is not good for the below method.
        # shortest path to (1, 1) is (0,0) -> (-1, 2) -> (1, 1).
        # 1. can set the range to :-1<=xx<=300 and 0-1<=yy<=300
        # or directly return (1, 1) result
        if x == 1 and y == 1: return 2
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1,), (-1, 2)]
        visited = set()
        # x, y, steps
        dq = collections.deque([(0, 0, 0)])
        while dq:
            curX, curY, curStep = dq.popleft()
            for d in dirs:
                xx, yy = curX + d[0], curY + d[1]
                if xx == x and yy == y:
                    return curStep + 1
                # or set a bigger range than x, y range: eg. -10<=xx<=310 and -10<=yy<=310
                if 0<=xx<=300 and 0<=yy<=300 and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    dq.append((xx, yy, curStep + 1))
                #print('dq: {}'.format(dq))

    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Runtime: 1855 ms, faster than 61.18% of Python online submissions for Minimum Knight Moves.
        # Memory Usage: 22.5 MB, less than 54.61% of Python online submissions for Minimum Knight Moves.
        # Time Complexity: O(V+E). V is node count. E is edge count.
        # Space: O(V).
        import collections
        # the board is symmetric
        x, y = abs(x), abs(y)
        if x == 0 and y == 0: return 0
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1,), (-1, 2)]
        visited = set()

        # x, y, steps
        dq = collections.deque([(0, 0, 0)])
        while dq:
            curX, curY, curStep = dq.popleft()
            for d in dirs:
                xx, yy = curX + d[0], curY + d[1]
                if xx == x and yy == y:
                    return curStep + 1
                if -5 <= xx <= 305 and -5 <= yy <= 305 and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    dq.append((xx, yy, curStep + 1))


obj = Solution()
t1 = 1
t2 = 1
print(obj.minKnightMoves(t1, t2))
