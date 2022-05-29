class Solution(object):
    def countArrangement1(self, N):
        """
        :type N: int
        :rtype: int
        """
        #Runtime: 104 ms, faster than 89.51% of Python online submissions for Beautiful Arrangement.
        #Memory Usage: 20 MB, less than 33.33% of Python online submissions for Beautiful Arrangement.

        cache = dict()
        def solve(idx, nums):
            # nums=[1..n]
            # idx: the number to be added in to the arragement
            if not nums: return 1
            # current pos, the nums can be added  for example, in the first invoking, key = 1, (1..n)
            # cache[key] : the number of beautiful arragement
            key = idx, tuple(nums)
            # the key has been traveled.
            if key in cache: return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                # meet the requirements
                if n % idx == 0 or idx % n == 0:
                    ans += solve(idx + 1, nums[:i] + nums[i+1:])
            cache[key] = ans
            return ans
        # pick the first number from [1..n]
        return solve(1, range(1, N + 1))
    def countArrangement(self, N):
        #Runtime: 1188 ms, faster than 55.41% of Python online submissions for Beautiful Arrangement.
        #Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Beautiful Arrangement.
        # my own solution:dfs traveling o(n^n)  space: o(1)
        def arrageList(pos,nums):
            if not nums: return 1
            res=0
            for i in range(0,len(nums)):
                if nums[i] % pos == 0 or pos % nums[i] == 0:
                    res+= arrageList(pos+1,nums[:i]+nums[i+1:])
            return res

        return arrageList(1,range(1,N+1))

   def countArrangement(self, n: int) -> int:
        # Runtime: 1416 ms, faster than 54.37% of Python3 online submissions for Beautiful Arrangement.
        # Memory Usage: 13.8 MB, less than 98.76% of Python3 online submissions for Beautiful Arrangement.
        # time
        def find(cur, pos):
            # all postions match
            if pos > cur:
                res[0] += 1
                return
            for i in range(1, cur+1):
                # matching 
                if i not in visited and (i%pos == 0 or pos%i==0):
                    visited.add(i)
                    find(cur, pos+1)
                    visited.remove(i)

        visited = set()
        res = [0]
        find(n,1)
        return res[0]
if __name__ == '__main__':
    object = Solution()
    s = 2


    print('---Start---')
    print s
    r = object.countArrangement(s)
    print(r)
    print('---End---')
