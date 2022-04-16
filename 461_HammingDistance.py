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
    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Runtime: 11 ms, faster than 96.50% of Python online submissions for Hamming Distance.
        # Memory Usage: 13.4 MB, less than 35.86% of Python online submissions for Hamming Distance.
        tmp = x ^ y
        res = 0
        while tmp:
            res += tmp & 1
            tmp = tmp >> 1
        return res

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Runtime: 14 ms, faster than 89.80% of Python online submissions for Hamming Distance.
        # Memory Usage: 13.3 MB, less than 64.72% of Python online submissions for Hamming Distance.
        return bin(x ^ y).count('1')
if __name__ == '__main__':
    object = Solution()
    A=  1
    y = 3
    print('---Start---')
    r = object.hammingDistance(A,y)
    print(r)
    print('---End---')
