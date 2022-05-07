class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #Runtime: 164 ms, faster than 93.22% of Python online submissions for Diagonal Traverse.
        #Memory Usage: 14.9 MB, less than 80.00% of Python online submissions for Diagonal Traverse.
        if not matrix or not matrix[0]: return []
        m = len(matrix)
        n= len(matrix[0])
        flag=0
        cur,step=0,1
        row,col=0,0
        res=[]
        while col<n and row<m:
            res.append(matrix[row][col])
            if row==0 and flag==0:
                flag=1
                cur+=1
                row=0
                col=cur-row
            elif col==n-1 and flag==0:
                flag=1
                cur+=1
                row+=1
                col=cur-row
            elif col==0 and flag==1:
                flag=0
                cur+=1
                col=0
                row=cur-col
            elif row==m-1 and flag==1:
                flag=0
                cur+=1
                col+=1
                row=cur-col
            else:
                if flag==0:
                    row-=1
                    col= cur-row
                else:
                    col-=1
                    row=cur-col
            if col==n and flag==1:
                row+=1
                col-=1
            if row==m and flag==0:
                col+=1
                row-=1
        return res
    
 def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        # Runtime: 280 ms, faster than 39.03% of Python3 online submissions for Diagonal Traverse.
        # Memory Usage: 17.9 MB, less than 37.18% of Python3 online submissions for Diagonal Traverse.
        # time: o(n) space: 0(n)
        x, y, dir = 0, 0, 1
        m, n = len(mat), len(mat[0])
        res = []
        for _ in range(m*n):
            res.append(mat[x][y])
            # inside elements
            if dir > 0:
                i, j = x-1, y+1
            else:
                i, j = x+1, y-1
            if 0<=i<m and 0<=j<n:
                x, y = i, j
            else:
                if dir >0:
                    # right side up
                    if y+1 < n:
                        y += 1
                    # top side up
                    else:
                        x += 1
                else:
                    # left down
                    if x+1 < m:
                        x += 1
                    # bottom down
                    else:
                        y += 1
                dir *= -1
        return res

if __name__ == '__main__':
    object = Solution()
    A=  [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]



    print('---Start---')
    r = object.findDiagonalOrder(A)
    print(r)
    print('---End---')
