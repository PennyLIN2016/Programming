class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        #Runtime: 72 ms, faster than 81.03% of Python online submissions for Unique Substrings in Wraparound String.
        #Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Unique Substrings in Wraparound String.
        # time:o(n) space:o(26)=o(1)
        import collections
        counted=collections.defaultdict(int)
        l=0
        for i in range(len(p)):
            if i>0 and (ord(p[i])==ord(p[i-1])+1 or (p[i]=='a'and p[i-1]=='z')):
                l+=1
            else:
                l=1
            counted[p[i]]=max(l,counted[p[i]])
        return sum(counted.values())


if __name__ == '__main__':
    object = Solution()
    A=  'zab'
    print('---Start---')
    r = object.findSubstringInWraproundString(A)
    print(r)
    print('---End---')
