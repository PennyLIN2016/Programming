class question(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type: List[[int,int]]
        """
        # store the nums and their indexes
        d = {}
        # return this list
        r = []

        for i, num in enumerate(nums):
            if target - num in d:
                r.append ([d[target - num], i])
            d[num] = i
        return r

if __name__ == '__main__':
    k = question()
    intlist = [1,2,3,4,5,6,7,8,9,10,11,12]
    target = 14
    try:
        print 'The nums :',intlist
        print 'The target :',target
        print 'The result :',k.twoSum(intlist,target)
    except:
        print 'ERROR!!'


