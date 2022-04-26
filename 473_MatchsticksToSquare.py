class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 1440 ms, faster than 47.75% of Python online submissions for Matchsticks to Square.
        #Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Matchsticks to Square.
        # dfs solution: travel all possible combinations.
        if not nums or len(nums)<4 :return False
        sumN=sum(nums)
        side,rem=divmod(sumN,4)
        if rem!=0 or max(nums)>side:return False
        sideList=[side]*4
        nums.sort(reverse=True)
        return self.dfs(nums,0,sideList)
    def dfs(self,nums,index,sides):
        if index==len(nums):return True
        num=nums[index]
        for i in range(4):
            if sides[i]>=num:
                sides[i]-=num
                if self.dfs(nums,index+1,sides):return True
                sides[i]+=num
        return False
    
        def makesquare1(self, matchsticks: list[int]) -> bool:
        # 184 / 185 test cases passed.
        # this solution failed at [13,11,1,8,6,7,8,8,6,7,8,9,8]: should be true
        # because once find a combination of target side,
        # this combination will not be removed if the left sticks can match.
        # and the left elements can't match.
        lenSum, l = sum(matchsticks), len(matchsticks)
        if lenSum % 4 != 0:
            return False
        total = lenSum // 4
        # start for bigger number to decrease the dfs depth
        matchsticks.sort(reverse=True)
        print('new list: {}'.format(matchsticks))
        if matchsticks[-1] > total:
            return False
        visited = set()

        def ismatch(i, target):
            print('i-{} target-{} visited: {}'.format(i, target, visited))
            if target == 0:
                return True
            if target <= 0:
                return False
            for j in range(i, l):
                if j in visited:
                    continue
                visited.add(j)
                if matchsticks[j] == target:
                    print('v-1: {}'.format(visited))
                    return True
                if target > matchsticks[j] and ismatch(j+1, target - matchsticks[j]):
                    print('v-2: {}'.format(visited))
                    return True
                visited.remove(j)
            print('v-3: {}'.format(visited))
            print('i-{} target-{} True'.format(i, target))
            return False

        print('total:{}'.format(total))
        for v in range(l):
            if not ismatch(v, total):
                print('r-1')
                return False
        if len(visited) != l:
            print('r-2')
            print('v-{}'.format(visited))
            return False
        print('r-3')
        return True

    def makesquare2(self, matchsticks: list[int]) -> bool:
        # Runtime: 2153 ms, faster than 65.51% of Python3 online submissions for Matchsticks to Square.
        # Memory Usage: 14 MB, less than 55.63% of Python3 online submissions for Matchsticks to Square.
        lenSum= sum(matchsticks)
        total = lenSum // 4
        if lenSum % 4 != 0 or max(matchsticks) > total:
            return False

        def dfs(index):
            # all sticks have been put in to sides.
            # True for the whole dfs
            # the solution will not be ok until going into this line.
            if index == len(matchsticks):
                return True
            value = matchsticks[index]
            # a good solution has to match 4 combinations
            for i in range(4):
                # put the stick to one side
                # from greater number
                print('index:{} target[{}]-{}'.format(index, i, targets))
                if targets[i] >= value:
                    targets[i] -= value
                    if dfs(index+1):
                        # is good for this side
                        print('dfs-true-index:{} target-{}'.format(index, targets))
                        return True
                    # use the index to try next side.
                    targets[i] += value
            print('False:index:{} target[{}]-{}'.format(index, i, targets))
            return False

        targets = [total] * 4
        print('the original target -{}'.format(targets))
        # start for bigger number to decrease the dfs depth
        matchsticks.sort(reverse=True)
        print('new list: {}'.format(matchsticks))
        return dfs(0)

    def makesquare3(self, matchsticks: list[int]) -> bool:
        # Runtime: 2148 ms, faster than 65.51% of Python3 online submissions for Matchsticks to Square.
        # Memory Usage: 14 MB, less than 29.98% of Python3 online submissions for Matchsticks to Square.

        sumN = sum(matchsticks)
        side, rem = divmod(sumN, 4)
        if rem != 0 or max(matchsticks) > side: return False

        def dfsk(index):
            if index == len(matchsticks): return True
            num = matchsticks[index]
            for i in range(4):
                if sideList[i] >= num:
                    sideList[i] -= num
                    if dfsk(index + 1): return True
                    sideList[i] += num
            return False

        sideList = [side] * 4
        matchsticks.sort(reverse=True)
        return dfsk(0)


if __name__ == '__main__':
    object = Solution()
    A=  [1,1,2,2,2]
    print('---Start---')
    r = object.makesquare(A)
    print(r)
    print('---End---')
