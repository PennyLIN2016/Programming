import math
import random
class Solution:
    # Runtime: 158 ms, faster than 78.21% of Python3 online submissions for Generate Random Point in a Circle.
    # Memory Usage: 24.2 MB, less than 43.02% of Python3 online submissions for Generate Random Point in a Circle.
    # math solution : time: 0(1)  space: o(1) 

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> list[float]:
        # a random distance to the centre within the whole circle
        # the sqrt() is to make up the offset from random.random()* self.r: more points are close to the centerac
        # random.random()* self.r: more points are close to the center : becaue the random is besed on r
        # cirecle area is based on r**2, so use sqrt() to make up the difference.
        seed = math.sqrt(random.random()) * self.r
        # a random radian: a random point in the circle perimeter
        radian = random.random() * 2 * math.pi
        x = self.x + seed * math.cos(radian)
        y = self.y + seed * math.sin(radian)
        return [x, y]




# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

if __name__ == '__main__':
    object = Solution()
    A= [4,14,2]

    print('---Start---')
    r = object.totalHammingDistance(A)
    print(r)
    print('---End---')
