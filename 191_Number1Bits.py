class Solution(object):
    # passed 85.54%
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        B_count = 0
        while n!=0:
            B_count += n & 1
            n = n>>1

        return B_count



if __name__ == '__main__':

    i = 128


    k = Solution()

    print (k.hammingWeight(i))