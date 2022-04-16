class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 124 ms, faster than 79.67% of Python online submissions for 132 Pattern.
        #Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for 132 Pattern.
        # greedy solution: time:o(n) space: o(n)

        if len(nums)<3:return False
        third=float('-inf')
        two=[]
        for i in range(len(nums)-1,-1,-1):
            # nums[i]<third<two[-1] , index of third > two`s
            if nums[i]<third: return True
            # two[-1] > third assume no duplicated element
            while two and two[-1]<nums[i]:
                third=two.pop()
            # index of two[-1] < thirds
            two.append(nums[i])
        return False
    
   def find132pattern2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 285 ms, faster than 100.00% of Python online submissions for 132 Pattern.
        #Memory Usage: 28.5 MB, less than 70.15% of Python online submissions for 132 Pattern.
        # time: o(n) space: o(n)
        l = len(nums)
        if l < 3:
            return False
        # left-mid-right: left<right<mid
        right = float('-inf')
        # store the value greater than right in order.
        # every value greater then right and in front of right can work as a mid
        mid = []
        for i in range(l-1, -1, -1):
            # mid has mid and nums[i] works as left
            # nums[i] < right < mid
            if nums[i] < right:
                return True
            while mid and mid[-1] < nums[i]:
                # if right<= nums[i] <= mid[-1]: just add a new possible mid value
                # if mid[-1] < nums[i]: find a new 32
                # right and mid both greater than left, so the solution is find suitable left
                # have to iterate in reversed order. 
                # if using normal order, to find suitable right, right is between [mid, left]
                # the solution can ensure mid is greater than right. 
                right = mid.pop()
            mid.append(nums[i])
        return False

if __name__ == '__main__':
    object = Solution()
    A=[-1, 3, 2, 0]
    print('---Start---')
    r = object.find132pattern(A)
    print(r)
    print('---End---')
