class Solution(object):
    def solveEquation1(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # Runtime: 20 ms, faster than 29.17% of Python online submissions for Solve the Equation.
        # Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Solve the Equation.
        # my solution: t(n)= o(n) space(n)= o(1)
        print('the input is   {}   '.format(equation))
        if not str : return "No solution"
        e= equation.split('=')
        print(e)
        if len(e)!=2 : return "No solution"
        else:
            left, right= e[0],e[1]
            a1,b1= self.getE(left)
            a2,b2=self.getE(right)
        if a1==a2:
            if b1==b2: return "Infinite solutions"
            else: return "No solution"
        else:
            return ('x='+ str((b2-b1)//(a1-a2)))
    def getE(self,strE):
        if not strE: return 0,0
        tmp,flag,a,b,pre=0,1,0,0,''
        for v in strE:
            print('v:'+str(v))
            if v =='-':
                b+=flag*tmp
                flag=-1
                tmp=0
            elif v=='+':
                b+=flag*tmp
                flag=1
                tmp=0
            elif v=='x':
                # for 'x=2' and '0x=0'
                if tmp==0 and pre!='0': tmp=1
                a+=flag*tmp
                flag=1
                tmp=0
            else:
                tmp= tmp*10+int(v)
            pre=v

            print((a, b))
        if tmp!=0:
            b+=flag*tmp
        print('go back to main()')
        return a,b



if __name__ == '__main__':
    object = Solution()
    #n1=["0:start:0","1:start:2","1:end:5","0:end:6"]
    #n2= 2
    n1= "x+5-3+x=6+x-2"
    #n1= "4x+6-3x=-x+4+2x+2"


    print('---Start---')
    print (n1)
    r = object.solveEquation(n1)
    print(r)
    print('---End---')
