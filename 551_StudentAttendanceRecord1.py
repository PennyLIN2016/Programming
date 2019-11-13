class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Runtime: 16 ms, faster than 77.26% of Python online submissions for Student Attendance Record I.
        #Memory Usage: 11.8 MB, less than 25.00% of Python online submissions for Student Attendance Record I.
        # my own solution: time: o(n), space:o(1)
        if not s: return False
        if 'LLL' in s:
            return False
        count=0
        for char in s:
            if char=='A':
                count+=1
            if count>=2:return False
        return True

if __name__ == '__main__':
    object = Solution()
    n1="PPALLP"

    print('---Start---')
    print n1
    r = object.checkRecord(n1)
    print(r)
    print('---End---')
