class Solution(object):
    # my solution 33s
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = [-float('inf')] + nums + [-float('inf')]
        for i in range(1,len(a)-1):
            if a[i] > a[i-1] and a[i] > a[i+1]:
                return i-1




if __name__ == '__main__':
    s = []
    k = Solution()
    print (k.findPeakElement(s))





