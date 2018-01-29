class question(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0])==0:
            return []

        h =len(matrix)
        w = len(matrix[0])
        list_after = []
        dir = 0 # 0 is horizontal and right; 1 is vertical and down; 2 is horizontal and left ;3 is vertical and up.
        i = 0
        j = 0
        while h>0 and w>0:
            if dir == 0:
                for x in xrange(j,j+w):
                    list_after.append(matrix[i][x])
                h -= 1
                dir = 1
                i+=1
                j+= w-1
            elif dir == 1:
                for y in xrange(i,i+h):
                    list_after.append(matrix[y][j])
                w -= 1
                dir = 2
                i+=h-1
                j-= 1
            elif dir == 2:
                for x in reversed(xrange(j-w+1,j+1)):
                    list_after.append(matrix[i][x])
                h -= 1
                dir = 3
                i-=1
                j-= w-1
            else: # dir == 3
                for y in reversed(xrange(i-h+1,i+1)):
                    list_after.append(matrix[y][j])
                w -= 1
                dir = 0
                i-=h-1
                j+= 1

        return list_after

if __name__ == '__main__':

    k = question()
    '''List_M = [
              [ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]
            ]'''

    #List_M = [[6,9,7]]
    List_M =[]

    r= k.spiralOrder(List_M)
    print r




