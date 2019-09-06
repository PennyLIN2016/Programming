class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 72.80% of Python online submissions for Hamming Distance.
        #Memory Usage: 11.7 MB, less than 68.18% of Python online submissions for Hamming Distance.
        # time:o(1) space:o(1)

        tmp= x^y
        res=0
        for i in range(32):
            if tmp&1==1:res+=1
            tmp>>=1
        return res

if __name__ == '__main__':
    object = Solution()
    A=  1
    y = 3
    print('---Start---')
    r = object.hammingDistance(A,y)
    print(r)
    print('---End---')
