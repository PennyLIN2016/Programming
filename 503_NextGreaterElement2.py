import collections
class Solution(object):
    def nextGreaterElements1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brutal solution: time out : 217 / 224 test cases passed.
        if not nums: return []
        max_n= max(nums)
        res=[]
        for i ,value in enumerate(nums):
            print("i: "+ str(i) + '  value: '+ str(value))
            print res
            if value == max_n:
                res.append(-1)
                continue
            for j in range(len(nums)):
                pos=(j+i+1)%len(nums)
                if nums[pos]>value:
                    res.append(nums[pos])
                    break
        return res
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 208 ms, faster than 64.26% of Python online submissions for Next Greater Element II.
        #Memory Usage: 13.8 MB, less than 25.00% of Python online submissions for Next Greater Element II.
        res=[-1]* len(nums)
        s=[]
        # the loop is executed twice
        for i in range(len(nums))*2:
            while s and (nums[s[-1]]<nums[i]):
                res[s.pop()]=nums[i]
            s.append(i)
        return res



if __name__ == '__main__':
    object = Solution()
    A= [1,2,1]
    print('---Start---')
    r = object.nextGreaterElements(A)
    print(r)
    print('---End---')
