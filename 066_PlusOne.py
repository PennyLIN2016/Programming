class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []

        digits[-1]+= 1
        if digits[-1]< 10:
            return digits
        digits[-1] -= 10
        carry_bit = 1
        for i in reversed(xrange(len(digits)-1)):
            digits[i] += carry_bit
            if digits[i] < 10:
                carry_bit = 0
                break
            digits[i] -= 10

        if carry_bit == 1:
            r = [1]+ digits[:]
            return r
        else:
            return digits

if __name__ == '__main__':

    #B = [2,4,5,6]
    #B =[9,9,9,9]
    B = [6,7,9,9]
    #B = [1,0]
    #B= [[1]]
    #B= [[0,0],[1,1],[0,0]]
    #B = [[1,0],[0,0]]
    #B = [[1,0]]
    #B = [[1,2],[1,1]]

    A = Solution()
    r = A.plusOne(B)
    print 'Result:',r





