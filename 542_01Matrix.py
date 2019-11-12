class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        #Runtime: 576 ms, faster than 82.25% of Python online submissions for 01 Matrix.
        #Memory Usage: 15.6 MB, less than 18.18% of Python online submissions for 01 Matrix.
        # google solution: bfs+ dp
        if not matrix or not matrix[0]: return matrix
        h,w = len(matrix),len(matrix[0])
        res=[[0]*w for x in range(h)]
        # put all 1 elements in to a queue: bfs
        undoQueue=[(x,y)for x in range(h) for y in range(w) if matrix[x][y]]
        # count the distance
        step=0
        while undoQueue:
            step+=1
            nq,mq=[],[]
            for i,j in undoQueue:
                zero=0
                # for directions
                for dx,dy in zip((1,0,-1,0),(0, 1, 0, -1)):
                    nx,ny=i+dx,j+dy
                    if 0<=nx<h and 0<=ny<w and matrix[nx][ny]==0:
                        zero+=1
                if zero:
                    res[i][j]=step
                    # reachable elements
                    mq.append((i,j))
                else:
                    # unreachable elements
                    nq.append((i,j))
            for i,j in mq:
                matrix[i][j]=0
            undoQueue=nq
        return res

if __name__ == '__main__':
    object = Solution()
    n1=[[0,0,0],
 [0,1,0],
 [0,0,0]]


    print('---Start---')
    print n1
    r = object.updateMatrix(n1)
    print(r)
    print('---End---')
