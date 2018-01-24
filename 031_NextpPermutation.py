class question(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) <= 1:
            return

        Pos_error = -1
        i = -1
        while i > -len(nums):
            if nums[i]> nums[i-1]:
                Pos_error = len(nums)+ i-1
                break
            i -=1

        if Pos_error == -1:
            self.reverse(nums,0,len(nums)-1)
            return

        min_pos,min_val = Pos_error+1, nums[Pos_error+1]

        for j in xrange(Pos_error+1,len(nums)):
            if nums[j]<= min_val and nums[j]> nums[Pos_error]:
                min_pos,min_val = j, nums[j]

        nums[min_pos],nums[Pos_error] = nums[Pos_error], nums[min_pos]
        self.reverse(nums,Pos_error+1,len(nums)-1)


    def reverse(self,list,head,end):

        while head< end:
            list[head],list[end] = list[end],list[head]
            head +=1
            end -=1


if __name__ == '__main__':

    #List = [1,2,3,4,5,6,7,8]
    #List = [8,7,6,5,4,3,2,1]
    List = [1,2,3,7,0,9,4,10,9,8,6]
    #List = None
    k = question()
    print 'input is :',List
    r= k.nextPermutation(List)
    print ' After Permutation: ', List



