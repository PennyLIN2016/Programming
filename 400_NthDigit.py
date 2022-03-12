class Solution(object):
    def findNthDigit1(self, n):
        """
        :type n: int
        :rtype: int
        """
        ##35 / 70 test cases passed.Status: Time Limit Exceeded
        # brutal solution: time: o(n)  space o(1)
        pre=0
        cur_n=1
        pos=0
        while n>=1:
            if pos>=len(str(cur_n)):
                pos=0
                cur_n+=1
            pre=str(cur_n)[pos]
            pos+=1
            n-=1
        return pre

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 12 ms, faster than 89.96% of Python online submissions for Nth Digit.
        #Memory Usage: 11.7 MB, less than 75.86% of Python online submissions for Nth Digit.
        # math solution: time : o(lgn): not sure. space:o(1)
        # 1 bit nubmer
        l=1
        m=9
        cur_head=1
        while n>l*m:
            # get the right length of nubmer
            n-=l*m
            l+=1
            m*=10
            cur_head*=10
        # get the right number
        # the first numer is 10000, so shoud use n-1, not n
        # number : 0...n-1
        cur_number = cur_head+ int((n-1)/l)
        # get the right bit in the right number
        return int(str(cur_number)[(n-1)%l])


if __name__ == '__main__':
    object = Solution()
    s = 10000000


    r = object.findNthDigit(s)
    print(r)
    print('---End---')
