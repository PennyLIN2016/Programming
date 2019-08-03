import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #Runtime: 12 ms, faster than 93.43% of Python online submissions for Evaluate Division.
        #Memory Usage: 11.7 MB, less than 92.71% of Python online submissions for Evaluate Division.
        # dfs solution: two-ways graph
        def dfs(x,y,table,visited):
            if x==y:
                return 1.0
            visited.add(x)
            for i in table[x]:
                if i in visited:continue
                visited.add(i)
                d= dfs(i,y,table,visited)
                if d>0:
                    return d*table[x][i]
            return -1.0

        table= collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0 / value
        res = [dfs(x,y,table,set()) if x in table and y in table else -1.0 for (x,y) in queries]
        return res


if __name__ == '__main__':
    object = Solution()
    s = [ ["a", "b"], ["b", "c"] ],
    k = [2.0, 3.0],
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]


    r = object.calcEquation(s,k,queries)
    print(r)
    print('---End---')
