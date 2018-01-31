class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def path_num(start,target):
            if start[0]==target[0] or start[1]==target[1]:
                return 1
            r = path_num([start[0]+1,start[1]],target)
            r+= path_num([start[0],start[1]+1],target)
            return r

        start= [1,1]
        target = [m,n]
        r = path_num(start,target)
        return r



if __name__ == '__main__':

    m = 2
    n = 2

    A = Solution()
    r = A.uniquePaths(m,n)
    print 'Result:',r





