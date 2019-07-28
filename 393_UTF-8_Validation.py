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


if __name__ == '__main__':
    object = Solution()
    k =  [197, 130, 1]


    r = object.validUtf8(k)
    print(r)
    print('---End---')
