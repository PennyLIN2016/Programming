class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Runtime: 12 ms, faster than 87.84% of Python online submissions for Number of Segments in a String.
        #Memory Usage: 11.7 MB, less than 36.36% of Python online submissions for Number of Segments in a String.
        if not s: return 0
        str1=s.split(' ')
        res=0
        for value in str1:
            if value:res+=1
        return res

if __name__ == '__main__':
    object = Solution()
    num = "Hello, my name is John"

    print(num)
    print('---Start---')
    r = object.countSegments(num)
    print(r)
    print('---End---')
