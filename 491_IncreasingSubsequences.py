class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Runtime: 240 ms, faster than 25.00% of Python online submissions for Increasing Subsequences.
        #Memory Usage: 24.1 MB, less than 100.00% of Python online submissions for Increasing Subsequences.
        res=set()
        print nums
        self.findSub(res,0,nums,[])
        print res
        # the return should be a list. if use list(res), the element in the list would still be tuple .
        return map(list,res)

    def findSub(self,cur,i,nums,path):
        print path
        if len(path)>=2:
            if tuple(path) not in cur:
                cur.add(tuple(path))
        for j in range(i,len(nums)):
            if not path or nums[j]>=path[-1]:
                self.findSub(cur,j+1,nums,path+[nums[j]])


if __name__ == '__main__':
    object = Solution()
    A= [4, 6, 7, 7]

    print('---Start---')
    r = object.findSubsequences(A)
    print(r)
    print('---End---')
