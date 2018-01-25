class question(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]

        right = len(nums)-1
        left = 0
        tar_right,tar_left = -1,-1
        while left >=0 and right< len(nums) and left <= right:
            mid = int((right+left)/2)
            if nums[mid]== target:
                tar_right,tar_left = mid,mid
                i = mid -1
                while  0<=i:
                    if nums[i]== target:
                        tar_left = i
                        i-=1
                    else:
                        break
                j = mid+1
                while j<= len(nums)-1:
                    if nums[j]== target:
                        tar_right = j
                        j+=1
                    else:
                        break
                return [tar_left,tar_right]
            elif nums[mid]< target:
                left = mid +1
            else:
                right = mid-1

        return [tar_left,tar_right]
if __name__ == '__main__':

    #List = [1,2,2,2,2,3,4,5,6,7,8]
    #List = [8,7,6,5,4,3,2,1]
    #List = [1,2,3,7,0,9,4,10,9,8,6]
    #List = None
    List = [1]

    target = 0
    k = question()
    print 'input is :',List
    r= k.searchRange(List,target)
    print ' result: ', r



