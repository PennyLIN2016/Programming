# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    # here the target number =6
    target= 89
    if num==target:return 0
    elif num>target:return -1
    else: return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 12 ms, faster than 92.79% of Python online submissions for Guess Number Higher or Lower.
        #Memory Usage: 11.7 MB, less than 73.28% of Python online submissions for Guess Number Higher or Lower.
        # time: o(lgn) space:o(1)
        left,right,cur=1,n,int((1+n)/2)
        #while True and left<=right:
        # assume the pick nubmer shall within [1,n]
        while True :
            tmp=guess(cur)
            if tmp==0: return cur
            elif tmp==1:
                left= cur+1
            elif tmp==-1:
                right= cur-1
            cur=int((left+right)/2)


       # return False

if __name__ == '__main__':
    object = Solution()
    k = 1290000


    r = object.guessNumber(k)
    print(r)
    print('---End---')
