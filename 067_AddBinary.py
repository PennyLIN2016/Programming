class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b

        if len(a)> len(b):
            b = '0'*(len(a)-len(b))+b
        else:
            a = '0'*(len(b)-len(a))+a

        carry_flag = 0
        s = ''
        i = -1
        while i >= -len(a):
            tmp = carry_flag + int(a[i])+int(b[i])
            if tmp >=2:
                carry_flag = 1
                s = str(tmp-2)+s
            else:
                carry_flag = 0
                s = str(tmp)+s
            i -= 1

        if carry_flag ==1:
            s = '1'+s

        return s



if __name__ == '__main__':

    a = '11'
    b= '1'

    A = Solution()
    r = A.addBinary(a,b)
    print 'Result:',r





