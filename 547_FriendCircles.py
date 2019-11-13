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



if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]


    print('---Start---')
    print n1
    r = object.findCircleNum(n1)
    print(r)
    print('---End---')
