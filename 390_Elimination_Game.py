class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 24 ms, faster than 90.58% of Python online submissions for Elimination Game.
        #Memory Usage: 11.7 MB, less than 80.00% of Python online submissions for Elimination Game.
        # math solution: time: o(lgn) space: o(1)
        DirFlag= True
        t=1
        # the first item in the current left list
        head=1
        # n is the current length of left list
        while n>1:
            if DirFlag is True or n%2==1:
            # only if the direction is leftto right or from right to left, but the lenght of left list is odd.
                head+= t
            n= int(n/2)
            DirFlag= not DirFlag
            # the step between two element in left list
            t*=2

        return head

if __name__ == '__main__':
    object = Solution()
    k = 108

    r = object.lastRemaining(k)
    print(r)
    print('---End---')
