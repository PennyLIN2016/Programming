class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # Runtime: 16 ms, faster than 79.17% of Python online submissions for Fraction Addition and Subtraction.
        # Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Fraction Addition and Subtraction.
        # google solution:
        if not expression: return "0/1"
        # f : list of fractions
        part=''
        f=[]
        for val in expression:
            if val in '+-':
                if part:
                    f.append(part)
                    part=''
            part+=val
        if part:
            f.append(part)

        # numerator list
        ns=[int(e.split("/")[0]) for e in f]
        # denominator list
        ds=[int(e.split("/")[1]) for e in f]
        import functools
        # lcm of all denominator
        d= functools.reduce(self.lcm,ds)
        # sum of numerator
        n=sum(h*d /l for h,l in zip(ns,ds))
        g=abs(self.gcd(n,d))
        return (str(int(n/g))+"/"+str(int(d/g)))

    # get the gcd
    def gcd(self,a,b):
        if a<b: a,b=b,a
        while b:
            a,b=b,a%b
        return a

    def lcm(self,a,b):
        return a*b /self.gcd(a,b)

    ### python3
        def fractionAddition1(self, expression: str) -> str:
        # Runtime: 44 ms, faster than 47.95% of Python3 online submissions for Fraction Addition and Subtraction.
        # Memory Usage: 13.9 MB, less than 80.70% of Python3 online submissions for Fraction Addition and Subtraction.
        # math solution eval; o(len(expression)) space: o(1)
        import fractions
        v = fractions.Fraction(eval(expression)).limit_denominator().as_integer_ratio()
        return '{}/{}'.format(v[0], v[1])

    def fractionAddition(self, expression: str) -> str:
        #Runtime: 66 ms, faster than 11.11% of Python3 online submissions for Fraction Addition and Subtraction.
        # Memory Usage: 13.9 MB, less than 80.70% of Python3 online submissions for Fraction Addition and Subtraction.

        import functools
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a%b
            return a
        def lcm(a, b):
            return a*b / gcd(a,b)

        part = ''
        fractions = []
        for s in expression:
            # get a fraction number
            if s in '+-':
                if part: fractions.append(part)
                part = ''
            part += s
        if part: fractions.append(part)
        numerators = [int(v.split('/')[0]) for v in fractions]
        denumerators = [int(v.split('/')[1]) for v in fractions]
        n2 = functools.reduce(lcm, denumerators)
        n1 = sum(h*n2/l for h, l in zip(numerators, denumerators))
        m = abs(gcd(n1, n2))
        return '{}/{}'.format(int(n1/m), int(n2/m))

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 ="-1/2+1/2+1/3"
    print('---Start---')
    print (n1)
    r = object.fractionAddition(n1)
    print(r)
    print('---End---')
