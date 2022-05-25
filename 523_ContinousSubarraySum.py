class Solution(object):
    def checkSubarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # brutal solution: 79 / 88 test cases passed. timeout

        if not nums or len(nums)<2: return False
        if k==0 :return False
        for i in range(2,len(nums)+1):
            for j in range(len(nums)-(i-1)):
                tmp=sum(nums[j:j+i])
                if tmp==0:
                    return True
                if tmp%k==0:
                    return True
        return False

    def checkSubarraySum(self, nums, k):
        #Runtime: 200 ms, faster than 41.64% of Python online submissions for Continuous Subarray Sum.
        #Memory Usage: 12.1 MB, less than 75.00% of Python online submissions for Continuous Subarray Sum.
        # time complexity o(n) space complexity o(n)
        # save the pos of the sum for m
        dmap={0:-1}
        total=0
        for i,n in enumerate(nums):
            # sum of [:i]
            total+=n
            m= total%k if k else total
            # a new vaule: dmap[m]: the lest index for m
            if m not in dmap:dmap[m]=i
            # the len>=2 : sum of [m+1:i] %k ==0
            elif dmap[m]+1<i: return True
        return False
    def checkSubarraySum1(self, nums: list[int], k: int) -> bool:
        # timeout: 94 / 95 test cases passed.
        # time: o(n*k) space: o(n *k)
        if len(nums) < 2:
            return False
        if k == 1:
            return True
        dp = [set() for _ in range(len(nums))]
        dp[0].add(nums[0] % k)
        for i in range(1, len(nums)):
            cur = nums[i] % k
            if (k-cur) % k in dp[i-1]:
                return True
            else:
                dp[i].add(cur)
                for v in dp[i-1]:
                    r = (cur + v) % k
                    if r not in dp[i]:
                        dp[i].add(r)
        return False
    def checkSubarraySum2(self, nums: list[int], k: int) -> bool:
        # timeout: 94 / 95 test cases passed.
        # time: o(n*k) space: o(1)
        if len(nums) < 2:
            return False
        if k == 1:
            return True
        preSet = set()
        preSet.add(nums[0] % k)
        for i in range(1, len(nums)):
            cur = nums[i] % k
            curSet = set()
            #print('nums[i]: {} cur: {}'.format(nums[i], cur))
            if (k-cur) % k in preSet:
                return True
            else:
                curSet.add(cur)
                for v in preSet:
                    r = (cur + v) % k
                    if r not in curSet:
                        curSet.add(r)
            preSet = curSet
        return False
    
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # Runtime: 1223 ms, faster than 38.87% of Python3 online submissions for Continuous Subarray Sum.
        # Memory Usage: 34.4 MB, less than 5.05% of Python3 online submissions for Continuous Subarray Sum.
        # time: o(n) space: (n)
        # sum of [:i]
        pre = [0]
        cur = 0
        for v in nums:
            cur += v
            pre.append(cur)
        # reminderDict[r]: the first pos of the reminder 
        reminderDict = {}
        for i in range(len(pre)):
            r = pre[i] % k
            if r not in reminderDict:
                reminderDict[r] = i
            else:
                # sum of [reminderDict[r]: i] is a match
                if i - reminderDict[r] >= 2:
                    return True
        return False


if __name__ == '__main__':
    object = Solution()
    A= [23, 2, 4, 6, 7]
    b=6



    print('---Start---')
    print A
    r = object.checkSubarraySum(A,b)
    print(r)
    print('---End---')
