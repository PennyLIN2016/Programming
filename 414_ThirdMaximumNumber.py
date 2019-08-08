class Solution(object):
    def thirdMax1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 36 ms, faster than 86.05% of Python online submissions for Third Maximum Number.
        #Memory Usage: 12.3 MB, less than 85.00% of Python online submissions for Third Maximum Number.
        #brutal solution: time : o(n) time: o(1)
        if len(nums)==1: return nums[0]
        res=[0]*3
        res[0]= nums[0]
        res[2]=float('-inf')
        pos=1
        while pos<len(nums):
            if nums[pos]!=res[0]:
                res[0] =max(nums[0],nums[pos])
                res[1]= min(nums[0],nums[pos])
                break
            pos+=1
        for i in range(pos,len(nums)):
            if nums[i] in res or nums[i]<res[2]:
                continue
            elif nums[i]<res[1]:
                res[2]=nums[i]
            elif nums[i]<res[0]:
                res[2]=res[1]
                res[1]=nums[i]
            else:
                res[2]=res[1]
                res[1]=res[0]
                res[0]=nums[i]
        return res[2] if res[2]!=float('-inf') else res[0]
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 36 ms, faster than 86.05% of Python online submissions for Third Maximum Number.
        #Memory Usage: 13 MB, less than 30.00% of Python online submissions for Third Maximum Number.
        # set solution: set will remove all duplicated elements.
        # suitable for all k value
        # time: o(n) space: o(n)
        tmp=set(nums)
        if len(tmp)<3: return max(tmp)
        k=2
        while k>0:
            k-=1
            tmp.remove(max(tmp))
        return max(tmp)


if __name__ == '__main__':
    object = Solution()
    num = [2, 2, 2, 1]

    print(num)
    r = object.thirdMax(num)
    print(r)
    print('---End---')
