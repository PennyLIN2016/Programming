class question(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        r_m = [[0] * n for _ in range(n)]
        # [[0] * n]*n , n copies of one original [[0] * n]. all copies should hold the same values.

        list_after = []
        dir = 0 # 0 is horizontal and right; 1 is vertical and down; 2 is horizontal and left ;3 is vertical and up.
        i = 0
        j = 0
        number = 1
        h, w= n,n
        while number<= n*n:
            if dir == 0:
                for x in xrange(j,j+w):
                    r_m[i][x] = number
                    number+= 1
                h -= 1
                dir = 1
                i+=1
                j+= w-1
            elif dir == 1:
                for y in xrange(i,i+h):
                    r_m[y][j]= number
                    number+=1
                w -= 1
                dir = 2
                i+=h-1
                j-= 1
            elif dir == 2:
                for x in reversed(xrange(j-w+1,j+1)):
                    r_m[i][x] = number
                    number +=1
                h -= 1
                dir = 3
                i-=1
                j-= w-1
            else: # dir == 3
                for y in reversed(xrange(i-h+1,i+1)):
                    r_m[y][j] = number
                    number+=1
                w -= 1
                dir = 0
                i-=h-1
                j+= 1

        return r_m

if __name__ == '__main__':

    k = question()


    #List_M = [[6,9,7]]
    N = 1
    r= k.generateMatrix(N)
    print r




