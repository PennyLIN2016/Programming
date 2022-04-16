class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 880 ms, faster than 14.28% of Python online submissions for Circular Array Loop.
        #Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Circular Array Loop.
        # time :o(n**2) space:o(1)
        # get the next index
        def nextpos(index,lists):
            return(index+lists[index])%len(lists)
        for i in range(len(nums)):
            slow=i
            fast=nextpos(slow,nums)
            # guarantee the same direction
            while nums[fast]*nums[i]>0 and nums[nextpos(fast,nums)]*nums[i]>0:
                if fast==slow:
                    if slow ==nextpos(slow,nums):
                        # the length is 1
                        break
                    return True
                # guarantee the time complexity is o(n)
                slow=nextpos(slow,nums)
                fast=nextpos(nextpos(fast,nums),nums)
        return False
     def circularArrayLoop1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 398 ms, faster than 44.26% of Python online submissions for Circular Array Loop.
        #Memory Usage: 13.6 MB, less than 19.67% of Python online submissions for Circular Array Loop.
        # brutal solution: 
        # time: o(n**2) space: o(n)
        def isCircle(start):
            cur = start
            visited = set()
            visited.add(cur)
            deep = 1
            while True:
                if (nums[cur] > 0) != (nums[start] > 0):
                    print('start-{} cur-{} resut: False'.format(start, cur))
                    return False
                j = (cur + nums[cur]) % l
                print('start-{} cur-{} j: {} visited: {}'.format(start, cur, j, visited))
                if j not in visited:
                    deep += 1
                    visited.add(j)
                    cur = j
                else:
                    if j == start and deep > 1:
                        return True
                    else:
                        return False

        l = len(nums)
        if l < 2:
            return False
        for i in range(l):
            if isCircle(i):
                return True
        return False


if __name__ == '__main__':
    object = Solution()
    A=[2,-1,1,2,2]
    print('---Start---')
    r = object.circularArrayLoop(A)
    print(r)
    print('---End---')
