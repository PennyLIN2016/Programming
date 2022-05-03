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

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        # Runtime: 315 ms, faster than 46.76% of Python3 online submissions for Increasing Subsequences.
        # Memory Usage: 22.7 MB, less than 23.22% of Python3 online submissions for Increasing Subsequences.
        # recursion solution

        def dfs(start, cur):
            if start == l-1:
                return
            cur.append(nums[start])
            print('res: {} cur-orig: {} start: {}'.format(res, cur, start))
            for i in range(start+1, l):
                print('i: {}'.format(i))
                if nums[i] >= nums[start]:
                    # if res is list, the solution would be timeout
                    # for [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
                    # if cur+[nums[i]] not in res would raise "TypeError: unhashable type: 'list'"
                    # Set members must be hashable.
                    if tuple(cur+[nums[i]]) not in res:
                        res.add(tuple(cur+[nums[i]]))
                        print('add one to res: {}'.format(res))
                    dfs(i, cur[:])
                    #cur.pop()
                    print('cur-after: {}'.format(cur))

        res = set()
        l = len(nums)
        for index in range(l-1):
            dfs(index, [])
        return map(list, res)

    def findSubsequences1(self, nums: list[int]) -> list[list[int]]:
        #Runtime: 242 ms, faster than 75.20% of Python3 online submissions for Increasing Subsequences.
        #Memory Usage: 20.6 MB, less than 98.89% of Python3 online submissions for Increasing Subsequences.
        # recursion solution time: o(n**2) space:o(n)
        res = set()
        self.dfs(nums, 0, res, [])
        return list(res)

    def dfs(self, nums, index, res, path):
        if len(path) >= 2:
            # make sure the path would not changed by later steps
            res.add(tuple(path))
        for i in range(index, len(nums)):
            if not path or nums[i] >= path[-1]:
                self.dfs(nums, i + 1, res, path + [nums[i]])
                
if __name__ == '__main__':
    object = Solution()
    A= [4, 6, 7, 7]

    print('---Start---')
    r = object.findSubsequences(A)
    print(r)
    print('---End---')
