class question(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n< 0:
            n = -n
            x = 1/x

        pow_sum = 1
        while n:
            if n & 1:# n is odd.
                pow_sum *= x
            x *= x
            n >>= 1
        return pow_sum

if __name__ == '__main__':
    try:
        k = question()
        x = 2.1000
        n = -3
        r= k.myPow(x,n)
        print r
    except:
        print 'Error!!!'



