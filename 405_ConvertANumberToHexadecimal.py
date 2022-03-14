class Solution(object):
   def toHex1(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Runtime: 18 ms, faster than 81.15% of Python online submissions for Convert a Number to Hexadecimal.
        #Memory Usage: 13.6 MB, less than 13.93% of Python online submissions for Convert a Number to Hexadecimal.
        # 32 bits
        k = 8
        flag = 0
        res = ''
        dictLetters = {10: 'a', 11: 'b', 12: 'c', 13:'d', 14: 'e', 15: 'f'}
        while k:
            k -= 1
            # get most 4 bits
            tmp = (num&0xf0000000)>>28
            # Skip leading 0
            if tmp != 0:
                flag = 1
            if flag:
                if tmp < 10:
                    res += str(tmp)
                else:
                    res += dictLetters[tmp]
            num <<= 4
        return res if res != '' else '0'
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        #For negative integers, two's complement method is used.
        #In computer,negative integers have been saved as complement number,
        #So do not worry about how to convert negative to complement number representation
        # Runtime: 23 ms, faster than 60.66% of Python online submissions for Convert a Number to Hexadecimal.
        # Memory Usage: 13.3 MB, less than 94.26% of Python online submissions for Convert a Number to Hexadecimal.
        if not num:
            return '0'
        res = []
        hexStr = '0123456789abcdef'
        # 32 bits = 8 chars
        while num and len(res)!= 8:
            # get the most right 4 bit: in hex, a char for 4 bits
            res.append(hexStr[num&15])
            num >>= 4
        return ''.join(res[::-1])






if __name__ == '__main__':
    object = Solution()
    num = 0

    print(num)
    r = object.toHex(num)
    print(r)
    print('---End---')
