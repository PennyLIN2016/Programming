class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #Runtime: 20 ms, faster than 69.37% of Python online submissions for Reverse String II.
        #Memory Usage: 12.1 MB, less than 55.56% of Python online submissions for Reverse String II.
        if not s or k<=1: return s
        tmpL=list(s)
        for i in range(0,len(tmpL),2*k):
            if len(tmpL)-i>=k:
                tmpL[i:i+k]=reversed(tmpL[i:i+k])
            else:
                tmpL[i:len(tmpL)]=reversed(tmpL[i:len(tmpL)])
        return "".join(tmpL)
    
        def reverseStr(self, s: str, k: int) -> str:
        #Runtime: 53 ms, faster than 36.93% of Python3 online submissions for Reverse String II.
        #Memory Usage: 14.1 MB, less than 57.30% of Python3 online submissions for Reverse String II.
        # time: o(n) space: o(1)

        def reverseSubStr(left, right):
            print('left: {}, right: {}'.format(left, right))
            while left < right:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1

        sList = list(s)
        tail = len(sList)
        print('tail: {} sList:{}'.format(tail, sList))
        for start in range(0, tail, 2*k):
            if tail -1 < start + k -1:
                print('tail-1: {} start:{}'.format(tail-1, start))
                reverseSubStr(start, tail-1)
            else:
                print('end: {} start:{}'.format(start + k -1, start))
                reverseSubStr(start, start + k -1)

        return ''.join(sList)


if __name__ == '__main__':
    object = Solution()
    n1="abcdefg"
    k = 8


    print('---Start---')
    print n1
    r = object.reverseStr(n1,k)
    print(r)
    print('---End---')
