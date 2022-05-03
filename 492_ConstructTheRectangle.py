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

     def constructRectangle(self, area: int) -> list[int]:
        # Runtime: 59 ms, faster than 35.10% of Python3 online submissions for Construct the Rectangle.
        # Memory Usage: 13.9 MB, less than 9.32% of Python3 online submissions for Construct the Rectangle.
        # force solution: time: o(lgn) space: o(1)
        import math
        w = int(math.sqrt(area))
        while w > 0:
            if area % w == 0:
                return [int(area/w), w]
            w -= 1



if __name__ == '__main__':
    object = Solution()
    A= 4

    print('---Start---')
    r = object.constructRectangle(A)
    print(r)
    print('---End---')
