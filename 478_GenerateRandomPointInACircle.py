import math
import random
class Solution(object):
#Runtime: 132 ms, faster than 90.73% of Python online submissions for Generate Random Point in a Circle.
#Memory Usage: 22.6 MB, less than 25.00% of Python online submissions for Generate Random Point in a Circle.
    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r=radius
        self.x=x_center
        self.y=y_center


    def randPoint(self):
        """
        :rtype: List[float]
        """

        # get a random radius, make sure the uniform random for circle point. not the uniform random between [0,radium]
        rr=math.sqrt(random.random())*self.r
        # get a uniform random alpha
        alpha= random.random()*2*3.141592653
        rx=self.x+rr*math.cos(alpha)
        ry=self.y+rr*math.sin(alpha)
        return [rx,ry]




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
