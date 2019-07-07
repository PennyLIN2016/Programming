class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #Runtime: 4 ms, faster than 99.64% of Python online submissions for Sum of Two Integers.
        #Memory Usage: 11.8 MB, less than 41.46% of Python online submissions for Sum of Two Integers.
        
        max_value=0x7FFFFFFF
        # make sure to get the last 32-bits
        mask_value =0xFFFFFFFF
        while b!=0:
            # a saves the bit sum result without carry bit. b saves the result of carry bit.
            # in next loop carry as b
            a,b= (a^b)&mask_value ,((a&b)<<1)&mask_value
        # if a is not negative , return a, otherwise get the complement firstly.
        return a if a<=max_value else ~(a^mask_value)







if __name__ == '__main__':
    k = Solution()
    x =1
    y= 2


    r = k.getSum(x,y)
    print(r)
    print('---End---')
