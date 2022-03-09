class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        #Runtime: 88 ms, faster than 84.92% of Python online submissions for UTF-8 Validation.
        #Memory Usage: 11.9 MB, less than 92.19% of Python online submissions for UTF-8 Validation.
        # time :o(n) space:o(1)
        # the next bytes belong to one num
        next= 0
        for v in data:
            if next==0:
                # a new num
                # start with 110
                if (v>>5)==0b110:next=1
                # start with 1110
                elif (v>>4)==0b1110:next=2
                # start with 11110
                elif (v>>3)==0b11110:next=3
                # not start with 0
                elif (v>>7): return False
            else:
                # not start with 10
                if (v>>6)!=0b10:return False
                next-=1
        return next==0
        
    def validUtf82(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def getByteType(num):
            r = 0
            base = 0b10000000
            while num >= 0:
                if num & base:
                    r += 1
                    base = base >> 1
                else:
                    return r
        
        expect = 0
        for v in data:
            t = getByteType(v)
            # UTF-8 encoding should be less than 4 bytes
            if t > 4: return False
            if expect == 0:
                if t == 1:
                    return False
                if t != 0:
                    expect = t-1
            else:
                if t != 1:
                    return False
                expect -= 1

        return expect == 0

if __name__ == '__main__':
    object = Solution()
    k =  [197, 130, 1]


    r = object.validUtf8(k)
    print(r)
    print('---End---')
