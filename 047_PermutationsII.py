
class question(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_next(nums,set_in,tmp,r):

            if len(tmp) == len(nums):
                r.append(tmp+[])
                # the [] makes sure the r.pop() will not discard the tmp.
                return

            for i in xrange(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and (i-1) in set_in:
                    continue
                if i not in set_in:
                    tmp.append(nums[i])
                    set_in.add(i)
                    permute_next(nums,set_in,tmp,r)
                    set_in.discard(i)
                    tmp.pop()

        if not nums:
            return []

        nums.sort()
        r = []
        tmp = []
        set_in = set()
        permute_next(nums,set_in,tmp,r)
        return  r

if __name__ == '__main__':

    List = [1,1,3]
    k = question()
    print 'input ',List
    r = k.permute(List)
    print  'result : ',r


