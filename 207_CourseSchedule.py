import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #Runtime: 72 ms, faster than 64.01% of Python online submissions for Course Schedule.
        #Memory Usage: 14.6 MB, less than 5.20% of Python online submissions for Course Schedule.

        graph = collections.defaultdict(list)
        # the topo relationship
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        # check if each item is reachable.
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    # Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        # each prerequisite is reachable
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True

if __name__ == '__main__':
    s = 2
    t = [[1,0]]

    k = Solution()
    r = k.canFinish(s,t)

    print(r)
    print('---End---')
