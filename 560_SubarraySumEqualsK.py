import collections
class Solution(object):
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 58 / 80 test cases passed. time out
        # brutal solution: o(n*n) space :o(1)
        if not nums: return 0
        l=len(nums)
        res=0
        for i in range(l):
            curSum=0
            for j in range(i,l):
                curSum+=nums[j]
                if curSum==k: res+=1
        return res
    
   def subarraySum(self, nums: list[int], k: int) -> int:
        # force solution: timeout 72 / 92 test cases passed.
        # time: o(n**2)
        l = len(nums)
        sumList = [0]
        res = 0
        for i in range(l):
            sumList.append(sumList[-1] + nums[i])
        print('sum-{}'.format(sumList))
        for i in range(l+1):
            for j in range(i+1, l+1):
                if sumList[j] - sumList[i] == k:
                    res += 1
        return res
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Runtime: 88 ms, faster than 90.97% of Python online submissions for Subarray Sum Equals K.
        #Memory Usage: 14.2 MB, less than 8.00% of Python online submissions for Subarray Sum Equals K.
        # google solution: time : o(n) space :o(n)
        # dp[key] store the occurence times of  the sum[:pos-1] equals to key// sum[i:j] = sum[:j]-sum[:i]
        dp=collections.defaultdict(int)
        dp[0]=1
        curSum,res=0,0
        for i in range(len(nums)):
            curSum+=nums[i]
            # curSum- key=k so sum[x:i+1] = k
            if curSum-k in dp:
                res+=dp[curSum-k]
            dp[curSum]+=1
        return res


if __name__ == '__main__':
    object = Solution()
    n1=[1,1,1]
    k = 2


    print('---Start---')

    r = object.subarraySum(n1,k)
    print(r)
    print('---End---')
