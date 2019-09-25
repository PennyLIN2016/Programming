import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #Runtime: 12 ms, faster than 96.75% of Python online submissions for Construct the Rectangle.
        #Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Construct the Rectangle.
        for w in range(int(math.sqrt(area)),0,-1):
            if area%w==0:
                return [int(area/w),w]




if __name__ == '__main__':
    object = Solution()
    A= 4

    print('---Start---')
    r = object.constructRectangle(A)
    print(r)
    print('---End---')
