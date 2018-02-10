class question(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return

        red= 0
        white= 0
        for value in nums:
            if value == 0:
                red += 1
            elif value == 1:
                white += 1

        blue = len(nums)- red- white
        nums[:] = [0 for i in range(red)]\
               +[1 for i in range(white)]\
               +[2 for i in range(blue)]

if __name__ == '__main__':

    m = [0,2,1,0,1,1,2]
    t = question()
    t.sortColors(m)
    print  'result : ',m


