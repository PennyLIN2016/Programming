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

if __name__ == '__main__':
    object = Solution()
    A=[-1, 3, 2, 0]
    print('---Start---')
    r = object.find132pattern(A)
    print(r)
    print('---End---')
