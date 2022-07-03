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

#####python 3
    def solveEquation(self, equation: str) -> str:
        # Runtime: 35 ms, faster than 79.36% of Python3 online submissions for Solve the Equation.
        # Memory Usage: 13.9 MB, less than 87.16% of Python3 online submissions for Solve the Equation.
        # time: o(n) : length of the str space:o(1)
        def getSum(inputStr):
            import re
            match = re.findall('([-+]?[0-9x]+)', inputStr)
            if not match:
                return 0
            s1, s2 = 0, 0
            for m in match:
                flag = 1
                if m[0] == '+':
                    m = m[1:]
                if m[0] == '-':
                    m = m[1:]
                    flag = -1
                if m[-1] == 'x':
                    if len(m) == 1:
                        s2 += 1 * flag
                    else:
                        s2 += int(m[:-1]) * flag
                else:
                    s1 += int(m) * flag
            return s1, s2

        left, right = equation.split('=')[0], equation.split('=')[1]
        left1, left2 = getSum(left)
        right1, right2 = getSum(right)
        n, x = left1-right1, right2 - left2
        if x == 0:
            return 'Infinite solutions' if n == 0 else 'No solution'
        else:
            return 'x={}'.format(n//x) if n % x == 0 else 'No solution'

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
