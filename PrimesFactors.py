
class question(object):

    def Primes_factor(self, integer):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        num = 2
        while num*num <= integer:
            if integer % num == 0:
                flag = False
                for i, prime in enumerate(primes):
                    if num % prime == 0:
                        flag = True
                        break
                if not flag:
                    primes.append(num)
            num+= 1

        return primes


if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs.strip()
    #r = k.LongestPaliSubstring(inputs.strip())
    r = k.Primes_factor(int(inputs))
    print  '1-Result : ',r




