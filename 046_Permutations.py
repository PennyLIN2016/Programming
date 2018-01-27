
class question(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_next(nums,set_in,tmp,r):

            if len(tmp) == len(nums):
                r.append(tmp+[])
                return

            for i in xrange(len(nums)):
                if nums[i] not in set_in:
                    tmp.append(nums[i])
                    set_in.add(nums[i])
                    permute_next(nums,set_in,tmp,r)
                    set_in.discard(nums[i])
                    tmp.pop()

        if not nums:
            return []

        r = []
        tmp = []
        set_in = set()
        permute_next(nums,set_in,tmp,r)
        return  r

if __name__ == '__main__':

    List = [1,2,3]
    k = question()
    print 'input ',List
    r = k.permute(List)
    print  'result : ',r


