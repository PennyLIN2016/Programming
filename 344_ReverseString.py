class Solution(object):
    def reverseString1(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #Runtime: 172 ms, faster than 86.57% of Python online submissions for Reverse String.
        #Memory Usage: 18.7 MB, less than 67.51% of Python online submissions for Reverse String.
        # time : o(n) space:o(1)
        if not s: return
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
     def reverseString2(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            s[i], s[-1-i] = s[-1-i],s[i]

if __name__ == '__main__':
    k = Solution()
    l= ['']

    k.reverseString(l)
    print(l)
    print('---End---')



