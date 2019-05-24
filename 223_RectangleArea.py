class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #Runtime: 40 ms, faster than 96.01% of Python online submissions for Rectangle Area.
        #Memory Usage: 11.8 MB, less than 40.00% of Python online submissions for Rectangle Area.
        pos=[((A,B),(C,D)),((E,F),(G,H))]
        pos.sort()
        ((A,B),(C,D)),((E,F),(G,H))= pos
        s1= (D-B)*(C-A)+(G-E)*(H-F)
        x,y = (min(C,G)-max(E,A)),(min(D,H)-max(B,F))
        s2= 0
        # make sure there are some area overlapped
        if x>0 and y>0 :
            s2=x*y
        return s1-s2





if __name__ == '__main__':

    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2

    object = Solution()
    r = object.computeArea(A,B,C,D,E,F,G,H)

    print(r)
    print('---End---')

