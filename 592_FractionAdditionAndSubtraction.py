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


if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 ="-1/2+1/2+1/3"
    print('---Start---')
    print (n1)
    r = object.fractionAddition(n1)
    print(r)
    print('---End---')