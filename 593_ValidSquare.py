import math
class Solution(object):
    def validSquare1(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # Runtime: 20 ms, faster than 65.64% of Python online submissions for Valid Square.
        # Memory Usage: 11.8 MB, less than 12.50% of Python online submissions for Valid Square.
        # my own solution: time :o(1) space:o(1): be mindful of the (sqrt(a))**2 may not equals to a in codes, so do not use sqrt in this case.
        if not p1 or not p2 or not p3 or not p4: return False
        p= [p1,p2,p3,p4]
        p.sort()
        print (p)
        l= self.getSide(p[0],p[1])
        print (l)
        if l==0 or not (l==self.getSide(p[0],p[2])==self.getSide(p[1],p[3])==self.getSide(p[2],p[3])):
            return False
        print(self.getSide(p[1],p[2]))
        return 2*l==self.getSide(p[1],p[2])


    def getSide(self,a,b):
        if a==b: return 0
        return (a[0]-b[0])**2+(a[1]-b[1])**2

    def validSquare(self, p1, p2, p3, p4):
        # Runtime: 24 ms, faster than 34.66% of Python online submissions for Valid Square.
        # Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Valid Square.
        # google solution: time :o(1) space:o(1)
        s= set([self.getSide(p1, p2), self.getSide(p1, p3), self.getSide(p1, p4), self.getSide(p2, p3), self.getSide(p2, p4), self.getSide(p3, p4)])
        return 0 not in s and len(s)==2


#############python3 
    def validSquare1(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        # Runtime: 32 ms, faster than 95.48% of Python3 online submissions for Valid Square.
        # Memory Usage: 13.8 MB, less than 92.98% of Python3 online submissions for Valid Square.
        # math solution: time: o(1) space: o(1)
        import collections
        import math
        def distance(n1, n2):
            return math.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2)
        dis = [distance(p1, p2), distance(p1, p3), distance(p1, p4),
                   distance(p2, p3), distance(p2, p4), distance(p3, p4)]
        cnt = collections.Counter(dis)
        if len(cnt) != 2:
            return False
        side, diag = -1, -1
        print('cnt: {}'.format(cnt))
        for k, v in cnt.items():
            if v == 4 and side == -1:
                side = k
            elif v == 2 and diag == -1:
                diag = k
            else:
                return False
        print('2*(side ** 2): {} diag ** 2: {}'.format(int(2*(side ** 2)), int(diag ** 2)))
        return round(2*(side ** 2)) == round(diag ** 2)

    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        # Runtime: 32 ms, faster than 95.48% of Python3 online submissions for Valid Square.
        # Memory Usage: 13.8 MB, less than 92.98% of Python3 online submissions for Valid Square.
        # improved math solution
        import collections
        import math
        def distance(n1, n2):
            return math.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2)
        dis = [distance(p1, p2), distance(p1, p3), distance(p1, p4),
                   distance(p2, p3), distance(p2, p4), distance(p3, p4)]
        cnt = collections.Counter(dis)
        return len(cnt) == 2 and 0 not in cnt


if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]

    n1=[1, 0]
    n2=[-1, 0]
    n3=[0, 1]
    n4=[0, -1]
    print('---Start---')
    print (n1)
    r = object.validSquare(n1,n2,n3,n4)
    print(r)
    print('---End---')
