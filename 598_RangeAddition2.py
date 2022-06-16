class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # Runtime: 48 ms, faster than 92.70% of Python online submissions for Range Addition II.
        # Memory Usage: 14.2 MB, less than 33.33% of Python online submissions for Range Addition II.
        # my own solution : t(n):o(l) space:o(1)
        m1,m2=m,n
        for value in ops:
            m1=min(m1,value[0])
            m2=min(m2,value[1])
        return m1*m2
#####python3
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # if ops= [] the return would be float('inf')
        r, c = float('inf'), float('inf')
        for v in ops:
            r = min(r, v[0])
            c = min(c, v[1])
        return r*c

    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # Runtime: 89 ms, faster than 66.41% of Python3 online submissions for Range Addition II.
        # Memory Usage: 16 MB, less than 78.91% of Python3 online submissions for Range Addition II.
        # time: o(len(ops)) space: o(1)
        r, c = m, n
        for v in ops:
            r = min(r, v[0])
            c = min(c, v[1])
        return r*c

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1= 3
    n2= 3
    m= [[2,2],[3,3]]

    print('---Start---')
    print (n1)
    r = object.maxCount(n1,n2,m)
    print(r)
    print('---End---')
