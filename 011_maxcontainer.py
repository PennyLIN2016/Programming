
class question(object):

    def MaxArea1(self, Height):## o(n**n)
        """
        :type height: list[int]
        :rtype : int
        """
        maxA = 0
        for i in range(len(Height)):
            for j in range(len(Height)):
                if i!=j:
                    h = min(Height[i],Height[j])
                    maxA = max(maxA,abs((i-j)*h))
        return maxA

    def MaxArea(self, height):## o(n)

        maxA = 0
        left = 0
        right = len(height)-1

        while left < right:
            h = min(height[left],height[right])
            maxA = max(maxA,(right-left)*h)

            # keep the higher side, the higher side has not be used by the Area.
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxA

if __name__ == '__main__':

    k = question()
    inputs = [1,1]
    print 'Input :', inputs
    r = k.MaxArea(inputs)
    print  'Result : ',r



