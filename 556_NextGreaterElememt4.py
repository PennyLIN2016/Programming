
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 12 ms, faster than 89.43% of Python online submissions for Next Greater Element III.
        #Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Next Greater Element III.
        # google solution: time :o(l) space: o(l)
        s=list(str(n))
        l= len(s)
        i = l-1
        while i>0 and s[i]<=s[i-1]:
            i-=1
        if i==0: return -1
        self.reverse(s,i,l-1)
        for j in range(i,l):
            if s[j]>s[i-1]:
                self.swap(s,i-1,j)
                break
        res= int(''.join(s))
        return -1 if res>1<<31 else res

    def swap(self,nums,p1,p2):
        nums[p1],nums[p2]=nums[p2],nums[p1]

    def reverse(self,nums,i,j):
        for k in range(i, (i + j) / 2 + 1):
            self.swap(nums, k, i + j - k)


if __name__ == '__main__':
    object = Solution()
    #n1= [1000,100,10,2]
    n1=12443322

    print('---Start---')
    print n1
    r = object.nextGreaterElement(n1)
    print(r)
    print('---End---')
