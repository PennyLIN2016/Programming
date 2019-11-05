class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #Runtime: 8 ms, faster than 97.58% of Python online submissions for Complex Number Multiplication.
        #Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Complex Number Multiplication.

        def getPara(s):
            paras=s.split('+')
            return [int(paras[0]),int(''.join(paras[1][:-1]))]

        m1=getPara(a)
        print m1
        m2=getPara(b)
        print m2

        r1=m1[0]*m2[0]-m1[1]*m2[1]
        res='-'+str(-r1)if r1<0 else str(r1)
        res+='+'
        r2=m1[0]*m2[1]+m1[1]*m2[0]
        res+= '-'+str(-r2)if r2<0 else str(r2)
        res+='i'
        return res






if __name__ == '__main__':
    object = Solution()
    n1="1+-1i"
    n2= "1+-1i"


    print('---Start---')
    print n1
    r = object.complexNumberMultiply(n1,n2)
    print(r)
    print('---End---')
