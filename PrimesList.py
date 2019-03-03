import time
class question(object):

    def CountPrimes(self, integer):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        for i in range(2, integer+1):
            flag = False
            for prime in (primes):
                if i % prime == 0:
                    flag = True
                    break
            if not flag:
                primes.append(i)

        return primes


if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs.strip()
    #r = k.LongestPaliSubstring(inputs.strip())
    print time.strftime('%X %x %Z')

    r = k.CountPrimes(int(inputs))
    print  '1-Result : ',r
    print time.strftime('%X %x %Z')




