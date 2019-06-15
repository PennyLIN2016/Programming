class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #Runtime: 220 ms, faster than 80.00% of Python online submissions for Minimum Height Trees.
        #Memory Usage: 18.4 MB, less than 9.30% of Python online submissions for Minimum Height Trees.
        # time : 0(n)    space: O(n)
        # the best roots should be in the middle of the graph, that means the node should have the most neighbor node.
        # the solution is to find the leave node(just one neighbor) and remove these from the possible result. keep doing the loop until all left nodes with
        # the same number of neigbours

        if n==1: return [0]

        import collections
        # dict to save the nodes` neigbours
        n_graph= collections.defaultdict(set)
        for a1,a2 in edges:
            n_graph[a1].add(a2)
            n_graph[a2].add(a1)
        # deque to save the current leaves: the nodes should be removed.
        leave_que= collections.deque()
        for v1,v2 in n_graph.items():
            # leave node
            if len(v2)==1:
                leave_que.append(v1)
        # removing loop, if n=2, the last two nodes should be the neigbour each other. the mth of the two nodes should be the same.
        while n>2:
            l= len(leave_que)
            n-=l
            for _ in range(l):
                value= leave_que.popleft()
                # remove the node and find new leave node
                for j in n_graph[value]:
                    n_graph[j].remove(value)
                    if len(n_graph[j])==1:
                        leave_que.append(j)
        return list(leave_que)


if __name__ == '__main__':
    k = Solution()
    s = [[1, 0], [1, 2], [1, 3]]
    j = 4
    print s
    r = k.findMinHeightTrees(j,s)

    print(r)
    print('---End---')



