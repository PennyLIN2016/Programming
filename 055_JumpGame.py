class question(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def JumpBool(nums,start,can_flag):
            if can_flag[0]== True:
                return
            if start ==len(nums)-1 or start+nums[start] >=  len(nums) :
                can_flag[0]= True
                return


            for i in reversed(xrange(1,nums[start]+1)):
                if can_flag[0] == True:
                    break
                JumpBool(nums,start+i,can_flag)
            return

        if not nums:
            return False
        if len(nums)==1:
            return True

        can_flag = [False]
        JumpBool(nums,0,can_flag)
        return can_flag[0]


if __name__ == '__main__':

    k = question()
    A = [2,3,1,1,4]
    #A = [3,2,1,0,4]
    #A = [2,0]

    print A
    r= k.canJump(A)
    print r




