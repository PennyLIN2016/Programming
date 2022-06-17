class Solution(object):
    def triangleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 268 ms, faster than 50.46% of Python online submissions for Valid Triangle Number.
        # Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Valid Triangle Number.
        # my own solution; time:o(n**2)  ??? space:o(n**2)
        if len(nums)<3:return 0
        nums.sort()
        sumD= dict()
        res=0
        for i,value in enumerate(nums):
            print('-----'+str(i))
            if not value: continue
            for key in sumD:
                if key>value:res+=sumD[key]
            print(res)
            for j in range(i):
                k=nums[i]+nums[j]
                if k not in sumD:
                    sumD[k]=1
                else:
                    sumD[k] += 1
            print(sumD)
        return res
    def triangleNumber1(self, nums):
        # Runtime: 200 ms, faster than 79.32% of Python online submissions for Valid Triangle Number.
        # Memory Usage: 11.9 MB, less than 16.67% of Python online submissions for Valid Triangle Number.
        # google solution: time: o(nlgn) space: o(1)
        nums.sort()
        res=0
        for i in range(len(nums)-1,1,-1):
            l,r=0,i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    res+= r-1
                    r-=1
                else:
                    l+=1
        return res
    
    
    ####python3
        def triangleNumber(self, nums: list[int]) -> int:
        # Runtime: 1223 ms, faster than 77.97% of Python3 online submissions for Valid Triangle Number.
        # Memory Usage: 14.1 MB, less than 28.16% of Python3 online submissions for Valid Triangle Number.
        # time: o(n**2) space:o(1)
        # time: o(nlgn)
        nums.sort()
        res = 0
        # nums[i] is the longest side. so just need to check a+b > nums[i]
        # time: o(l**2)
        for i in range(len(nums)-1, -1, -1):
            short, mid = 0, i-1
            while short < mid:
                if nums[short] + nums[mid] > nums[i]:
                    res += mid - short
                    mid -= 1
                else:
                    short += 1
        return res
    
    
    

if __name__ == '__main__':
    object = Solution()
    n1=[2,2,3,4]

    print('---Start---')
    print (n1)
    r = object.triangleNumber(n1)
    print(r)
    print('---End---')
