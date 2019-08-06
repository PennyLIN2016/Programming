class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #Runtime: 32 ms, faster than 63.18% of Python online submissions for Fizz Buzz.
        #Memory Usage: 12.6 MB, less than 78.02% of Python online submissions for Fizz Buzz.
        # time: o(n) space:o(n)
        stack=[]
        k=1
        while k<=n:
            if k%15==0:
                stack.append('FizzBuzz')
            elif k%5==0:
                stack.append('Buzz')
            elif k%3==0:
                stack.append('Fizz')
            else:
                stack.append(str(k))
            k+=1
        return stack

if __name__ == '__main__':
    object = Solution()
    num = 18

    print(num)
    r = object.fizzBuzz(num)
    print(r)
    print('---End---')
