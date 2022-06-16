import collections
class Solution(object):
     def findLHS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 340 ms, faster than 27.17% of Python online submissions for Longest Harmonious Subsequence.
        # Memory Usage: 13.8 MB, less than 100.00% of Python online submissions for Longest Harmonious Subsequence.
        # my own solution: time o(2n)=o(n)   space:o(2n) = o(n)
        d= collections.Counter(nums)
        res=0
        for key in d:
            if key+1 in d:
                res= max(res,d[key]+d[key+1])
            if key-1 in d:
                res = max(res, d[key] + d[key + 1])
        return res

     def findLHS(self, nums):
        # Runtime: 284 ms, faster than 92.20% of Python online submissions for Longest Harmonious Subsequence.
        # Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Longest Harmonious Subsequence.
        # my own improved solution: time : o(n)   space: o(n)
        s=set(nums)
        d=collections.defaultdict(int)
        for value in nums:
            if (value+1) in s:
                d[value]+=1
            if (value-1) in s:
                d[value-1]+=1
        res=0
        for key in d:
            res=max(res,d[key])
        return res


####python3 
    def findLHS(self, nums: list[int]) -> int:
        #Runtime: 421 ms, faster than 53.95% of Python3 online submissions for Longest Harmonious Subsequence.
        #Memory Usage: 20.5 MB, less than 6.95% of Python3 online submissions for Longest Harmonious Subsequence.
        # time: o(n) space: o(n)
        import collections
        posDict = collections.defaultdict(list)
        for i, v in enumerate(nums):
            posDict[v].append(i)
        res = 0
        # if for k, v in list(posDict.items()): will raise RuntimeError: dictionary changed size during iteration
        for k, v in list(posDict.items()):
            if posDict[k+1] == [] and posDict[k-1] == []:
                continue
            l1, l2, l3 = len(posDict[k+1]),  len(posDict[k]), len(posDict[k-1])
            res = max(res, l1 + l2, l2 + l3)
        return res

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n= [1,1,1,1]

    print('---Start---')
    print (n)
    r = object.findLHS(n)
    print(r)
    print('---End---')
