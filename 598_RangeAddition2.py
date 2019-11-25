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