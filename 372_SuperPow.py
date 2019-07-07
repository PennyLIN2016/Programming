class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ##Runtime: 116 ms, faster than 53.18% of Python online submissions for Super Pow.
        #Memory Usage: 11.7 MB, less than 68.93% of Python online submissions for Super Pow.
        # time = o(n) space: o(1) n= len(b)
        if not b or a ==1: return 1
        res= 1
        for value in b:
            # for example,2**13= (2**10)*(2**3)
            # ((2**1)**10)*(2**3)
            res= (res**10)*(a**value)%1337
        return res

if __name__ == '__main__':
    k = Solution()
    x =2
    y=[1,1]


    r = k.superPow(x,y)
    print(r)
    print('---End---')
