
class question(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sub_next(nums,k,sub_list,r):
            r.append(sub_list)
            for i in xrange(k,len(nums)):
                if i== k:
                    sub_next(nums,i+1,sub_list+[nums[i]],r)
                else:
                    if nums[i]!= nums[i-1]:
                        sub_next(nums,i+1,sub_list+[nums[i]],r)


        r = []
        sub_list =[]
        nums.sort()
        # 0 : the first index of item to be added into the sub_list
        sub_next(nums,0,sub_list,r)
        return r


if __name__ == '__main__':
    inputs = [3,1,3]
    k = question()
    r = k.subsetsWithDup(inputs)
    print r





