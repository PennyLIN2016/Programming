class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        #Runtime: 156 ms, faster than 31.78% of Python online submissions for Assign Cookies.
        #Memory Usage: 13 MB, less than 66.67% of Python online submissions for Assign Cookies.
        # time: o(nlgn) space:o(1)
        res=0
        p1,p2=0,0
        g.sort()
        s.sort()
        while p1<len(g) and p2<len(s):
            while p2<len(s) and g[p1]>s[p2]:
                p2+=1
            if p2==len(s):break
            if g[p1]<=s[p2]:
                res+=1
                p2+=1
            p1+=1
        return res

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Runtime: 139 ms, faster than 89.20% of Python online submissions for Assign Cookies.
        # Memory Usage: 15 MB, less than 16.67% of Python online submissions for Assign Cookies.
        # time: o(nlgn) space: o(1)
        g.sort()
        s.sort()
        print('g-{} s-{}'.format(g, s))
        k, c = 0, 0
        res = 0
        while c < len(s) and k < len(g):
            if s[c] >= g[k]:
                res += 1
                c += 1
                k += 1
            else:
                c += 1
        return res





if __name__ == '__main__':
    object = Solution()
    A=[7,9,10,6]
    B=[5,8,11,2,3]
    print('---Start---')
    r = object.findContentChildren(A,B)
    print(r)
    print('---End---')
