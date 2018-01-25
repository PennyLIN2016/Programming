
class question(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ''
        if num1 == '' or num2=='':
            return ''

        r = [0]*(len(num1)+len(num2))
        for i , n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                r[i+j]  += int(n1)*int(n2)
                r[i+j+1] += r[i+j]/10
                r[i+j] %= 10

        while len(r)>1 and r[-1]==0:
            r.pop()

        return ''.join(map(str,r[::-1]))


if __name__ == '__main__':

    str1 = '13'
    str2 = '23'
    k = question()
    print 'input : %s * %s :'%(str1,str2)
    r = k.multiply(str1,str2)
    print  'result : ',r


