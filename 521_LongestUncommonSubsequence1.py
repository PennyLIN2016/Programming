class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        #Runtime: 12 ms, faster than 85.64% of Python online submissions for Longest Uncommon Subsequence I .
        #Memory Usage: 11.9 MB, less than 20.00% of Python online submissions for Longest Uncommon Subsequence I .

        if a==b:
            return -1
        if a=='' or b=='': return max(len(a),len(b))
        if len(a)>len(b):
            return len(a)
        else:
            return len(b)
       
     def findLUSlength(self, a: str, b: str) -> int:
        # Runtime: 37 ms, faster than 64.62% of Python3 online submissions for Longest Uncommon Subsequence I.
        # Memory Usage: 13.8 MB, less than 61.27% of Python3 online submissions for Longest Uncommon Subsequence I.
        if a == b : return -1
        return max(len(a), len(b))



if __name__ == '__main__':
    object = Solution()
    A= "abac"
    B= ""


    print('---Start---')
    print A
    r = object.findLUSlength(A,B)
    print(r)
    print('---End---')
