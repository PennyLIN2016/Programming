class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Runtime: 264 ms, faster than 14.49% of Python online submissions for Friend Circles.
        #Memory Usage: 21.1 MB, less than 11.11% of Python online submissions for Friend Circles.
        # google solution: time :o(n*n) space: o(1)
        def findFriend(M,Cur,l):
            for i in range(l):
                # is friend and not visited
                if M[Cur][i]==1:
                    # set to visited.
                    M[Cur][i]=M[i][Cur]=0
                    # dfs find other friends
                    findFriend(M,i,l)
        if not M or not M[0]: return 0
        n=len(M)
        res=0
        for c in range(n):
            if M[c][c]==1:
                res+=1
                findFriend(M,c,n)
        return res
    def findCircleNum1(self, isConnected: list[list[int]]) -> int:
        # Runtime: 297 ms, faster than 39.20% of Python3 online submissions for Number of Provinces.
        # Memory Usage: 14.3 MB, less than 76.99% of Python3 online submissions for Number of Provinces.
        # bfs + iteration time: O(n**2) space: o(n)
        leftCity = set([i for i in range(len(isConnected))])
        res = 0
        while leftCity:
            res += 1
            city = list(leftCity)[-1]
            leftCity.remove(city)
            stack = [city]
            while stack:
                tmp = []
                for start in stack:
                    for c in list(leftCity):
                        if isConnected[start][c] == 1:
                            leftCity.remove(c)
                            tmp.append(c)
                stack = tmp
        return res

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # Runtime: 216 ms, faster than 74.80% of Python3 online submissions for Number of Provinces.
        # Memory Usage: 14.7 MB, less than 28.71% of Python3 online submissions for Number of Provinces.
        # dfs+recursion solution: time: o(n*n/2) space: o(n)
        def dfs(index):
            visited[index] = 1
            for i in range(len(isConnected)):
                if i == index:
                    continue
                if isConnected[index][i] == 1 and visited[i] == 0:
                    dfs(i)

        visited = [0] * len(isConnected)
        res = 0
        for n in range(len(isConnected)):
            if visited[n] == 0:
                res += 1
                dfs(n)
        return res



if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]


    print('---Start---')
    print n1
    r = object.findCircleNum(n1)
    print(r)
    print('---End---')
