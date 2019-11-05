import collections
class Solution(object):
    def findPairs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #56 / 72 test cases passed. time out
        if not nums or len(nums)<2 or k<0: return 0
        nums.sort()
        res=0
        picked =[]
        for left in range(len(nums)):
            for right in range(left+1,len(nums)):
                if [nums[left],nums[right]] in picked:continue
                print ('left:'+str(left)+ 'right:'+str(right))
                if nums[right]-nums[left]==k:
                    res+=1
                    picked.append([nums[left],nums[right]])
                    print picked
        return res
    def findPairs(self, nums, k):
        #Runtime: 100 ms, faster than 94.72% of Python online submissions for K-diff Pairs in an Array.
        #Memory Usage: 13.2 MB, less than 77.78% of Python online submissions for K-diff Pairs in an Array.
        if k<0 : return 0
        res=0

        if k ==0:
            nC=collections.Counter(nums)
            for value in nC:
                if nC[value]>1:
                    res+=1
            return res
        nums=set(nums)
        for value in nums:
            if value+k in nums:
                res+=1
        return res

if __name__ == '__main__':
    object = Solution()
    n1=[1,1,1,1,1]
    n2=0

    print('---Start---')
    print n1
    r = object.findPairs(n1,n2)
    print(r)
    print('---End---')
