import collections
class Solution(object):
    #Runtime: 92 ms, faster than 45.22% of Python online submissions for Course Schedule II.
    #Memory Usage: 14.6 MB, less than 27.59% of Python online submissions for Course Schedule II.
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = collections.defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
        print(graph)
        r = []
        visited =[0]*numCourses
        for i in range(numCourses):
            if not self.check(graph,visited,i,r):
                return []
        return r
    def check(self,graph,visited,i,r):
        if visited[i]==1:
            return False
        if visited[i]==2:
            return True
        visited[i]=1
        for k in graph[i]:
            if not self.check(graph,visited,k,r):
                return False
        visited[i]=2
        r.append(i)
        return True



if __name__ == '__main__':
    s = 4
    t =  [[1,0],[2,0],[3,1],[3,2]]

    print(t)
    k = Solution()
    r = k.findOrder(s,t)

    print(r)
    print('---End---')

