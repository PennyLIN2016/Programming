
class question(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n<1:
            return [0]
        r = [0 for i in xrange(2**n)]
        r[1]= 1
        mask = 0x01
        i =1 # the i-th bit from right to left
        while i<n:
            mask <<= 1 # mask skip 1 bit each time
            for j in xrange(2**i):
                root = 2**i
                r[root+j]= r[root-j-1]|mask
            i+=1
        return r


if __name__ == '__main__':

    inputs = raw_input('input the N :  ')
    k = question()
    print 'Input :', inputs
    r = k.grayCode( int(inputs))
    for i in xrange(2**int(inputs)):
       print 'r[',i,']:', bin(r[i])





