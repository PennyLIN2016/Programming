class Solution(object):
    def arrayNesting1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 124 ms, faster than 20.81% of Python online submissions for Array Nesting.
        #Memory Usage: 24.7 MB, less than 20.00% of Python online submissions for Array Nesting.
        # my own solution: time:o(n) space: o(1)
        maxSize,self.cur=0,0
        for i in range(len(nums)):
            if nums[i] == -1:continue
            self.cur=0
            self.getSet(i, nums)
            if self.cur>maxSize:
                maxSize = self.cur
        return maxSize

    def getSet(self,index,s):
        if s[index]==-1:return
        next = s[index]
        self.cur+=1
        s[index]=-1
        self.getSet(next,s)

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 96 ms, faster than 85.68% of Python online submissions for Array Nesting.
        #Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Array Nesting.
        # google solution+ my own solution: no recursion solution: time: o(n) space:o(1)
        res=0
        for k in range(len(nums)):
            path,i=0,k
            while nums[i]!=-1:
                path+=1
                tmp=nums[i]
                nums[i] = -1
                i=tmp
            res=max(path,res)
        return res





if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 = [5,4,0,3,1,6,2]

    print('---Start---')
    print (n1)
    r = object.arrayNesting(n1)
    print(r)
    print('---End---')