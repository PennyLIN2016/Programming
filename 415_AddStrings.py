class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #Runtime: 36 ms, faster than 57.77% of Python online submissions for Add Strings.
        #Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Add Strings.
        # brutal solution: time:o(n) space:o(1)
        if not num1: return num2
        if not num2: return num1
        l1,l2=len(num1),len(num2)
        carry=0
        res=''
        while l1 or l2:
            if l1 and l2:
                tmp=int(num1[l1-1])+int(num2[l2-1])+carry
                l1-=1
                l2-=1
            elif l1==0:
                tmp=int(num2[l2-1])+carry
                l2-=1
            elif l2==0:
                tmp=int(num1[l1-1])+carry
                l1-=1
            carry=int(tmp/10)
            res=str(tmp%10)+res

        return '1'+res if carry else res
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Runtime: 46 ms, faster than 48.55% of Python online submissions for Add Strings.
        # Memory Usage: 13.5 MB, less than 90.78% of Python online submissions for Add Strings.
        # does not convert the str to integers directly.
        # time: o(n) space: o(1)

        res, carry, i = '', 0, 0
        while i < max(len(num1), len(num2)) or carry == 1:
            i += 1
            if i <= len(num1):
                n1 = ord(num1[-i]) - ord('0')
            else:
                n1 = 0
            if i <= len(num2):
                n2 = ord(num2[-i]) - ord('0')
            else:
                n2 = 0
            tmp = carry + n1 + n2
            if tmp > 9 :
                carry = 1
                tmp -= 10
            else:
                carry = 0
            res = chr(ord('0')+tmp) + res
        return res


if __name__ == '__main__':
    object = Solution()
    num = '100000'
    num2='9088'

    print(num)
    print(num2)
    print('-----------')
    r = object.addStrings(num,num2)
    print(r)
    print('---End---')
