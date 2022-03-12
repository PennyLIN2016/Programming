import collections
class Solution(object):
    def calcEquation1(self, equations, values, queries):
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
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #Runtime: 26 ms, faster than 44.29% of Python online submissions for Evaluate Division.
        #Memory Usage: 13.5 MB, less than 51.84% of Python online submissions for Evaluate Division.
        import collections
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        visited = set()
        for (x,y), v in zip(equations, values):
            g[x][y] = v
            g[x][y] = 1.0/v
            visited.add(x)
            visited.add(y)
        for i in visited:
            g[i][i] = 1.0
            for j in visited:
                for k in visited:
                    if g[j][i] and g[i][k]:
                        g[j][k] = g[j][i] *  g[i][k]
        res = []
        for i, j in queries:
            res.append(g[i][j] if g[i][j] else -1.0)
        return res

if __name__ == '__main__':
    object = Solution()
    s = [ ["a", "b"], ["b", "c"] ],
    k = [2.0, 3.0],
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]


    r = object.calcEquation(s,k,queries)
    print(r)
    print('---End---')
