class Solution(object):
    def findComplement1(self, num):
        """
        :type num: int
        :rtype: int
        """
        #Runtime: 20 ms, faster than 37.10% of Python online submissions for Number Complement.
        #Memory Usage: 11.7 MB, less than 57.14% of Python online submissions for Number Complement.
        mask = 1<<30
        while not(num & mask):
            mask=mask>>1
        res=0
        while mask:
            res=res<<1
            if not (num&mask) :res+=1
            mask=mask>>1
        return res


    def findComplement(self, num):
        #Runtime: 8 ms, faster than 97.45% of Python online submissions for Number Complement.
        #Memory Usage: 11.8 MB, less than 42.86% of Python online submissions for Number Complement.
        # bin(num)= 0b+ num in binary format : srting
        # ^ would not handle the leading zero of a number.
        print bin(num)
        print bin((1 << (len(bin(num)) - 2)) - 1)
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)



if __name__ == '__main__':
    object = Solution()
    A= 27
    print('---Start---')
    r = object.findComplement(A)
    print(r)
    print('---End---')
