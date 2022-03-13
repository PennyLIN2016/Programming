class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        #Runtime: 36 ms, faster than 56.45% of Python online submissions for Remove K Digits.
        #Memory Usage: 11.9 MB, less than 92.68% of Python online submissions for Remove K Digits.
        # other`s solution: time : o(n) space o(n)
        if not num or len(num)==k: return '0'
        stack=[]
        for value in num:
            #make sure to keep the old order
            # if the number is greater than the later one , remove the front one
            # remove the first k non-ascend values
            while stack and k and int(stack[-1])>int(value):
                stack.pop()
                k-=1
            stack.append(value)
        # k>1: the left numbers is in increasing order already
        # romove the greater ones
        while k:
            # remove the most right vlaues: whick should be greater the the left ones.
            stack.pop()
            k-=1
        # make sure remove all leading zero
        return str(int(''.join(stack)))




if __name__ == '__main__':
    object = Solution()
    num = "912000348567"
    k = 4

    print(num)
    r = object.removeKdigits(num,k)
    print(r)
    print('---End---')
