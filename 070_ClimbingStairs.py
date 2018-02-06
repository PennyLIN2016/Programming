import math
class question(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """


        if not n:
            return 0
        sum = 1# all 1 steps
        i_two = n /2
        for i in xrange(1, i_two+1):
            step_num = n - i
            sum += math.factorial(step_num)/(math.factorial(step_num-i)*math.factorial(i))
        return sum

if __name__ == '__main__':

    inputs = raw_input('input the N :  ')
    k = question()
    r = k.climbStairs(int(inputs))
    print  'result : ',r


