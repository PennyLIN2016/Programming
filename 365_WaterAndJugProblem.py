class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # bezout`s theorem: if  z = m*x+n*y so z should be the k*(gcd(x,y)) and z <=x+y
        # the solution is to check if z is k*gcd(greatest common divisor)
        #Runtime: 12 ms, faster than 95.39% of Python online submissions for Water and Jug Problem.
        #Memory Usage: 11.8 MB, less than 51.16% of Python online submissions for Water and Jug Problem.
        # time : o(lg(z+y)) space: o(1)
        def gcd(a,b):
            return a if b==0 else gcd(b,a%b)
        return z==0 or( (x+y)>=z and z% gcd(x,y)==0)
    def canMeasureWater2(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        def gcd(n1, n2):
            r = 1
            f = 1
            while r< n1 and r <n2:
                r +=1
                if n1%r == 0 and n2%r == 0:
                    f = r
            return f
        f = gcd(jug1Capacity,jug2Capacity)
        #  you must have targetCapacity liters of water contained within one or both buckets by the end.
        # so jug1Capacity+ jug2Capacity>= targetCapacity
        return (jug1Capacity+ jug2Capacity)>= targetCapacity and targetCapacity%f == 0


if __name__ == '__main__':
    k = Solution()
    x =5
    y=3
    z=4


    r = k.canMeasureWater(x,y,z)
    print(r)
    print('---End---')
