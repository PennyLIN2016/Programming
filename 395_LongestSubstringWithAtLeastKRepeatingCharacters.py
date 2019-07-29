class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 96.07% of Python online submissions for Longest Substring with At Least K Repeating Characters.
        #Memory Usage: 11.8 MB, less than 97.50% of Python online submissions for Longest Substring with At Least K Repeating Characters.
        # time : o(n) space: o(1)
        def sublongestStr(s,k,left,right):
            charCount=[0]*26
            # the count in s[left:right],not in s[pos1:pos2], so need to check the sub str in next recursion
            for i in xrange(left,right):
                charCount[ord(s[i])-ord('a')]+=1
            maxLen=0
            pos1=left
            while pos1<right:
                while pos1< right and charCount[ord(s[pos1])-ord('a')]<k:
                    pos1+=1
                pos2=pos1
                while pos2< right and charCount[ord(s[pos2])-ord('a')]>=k:
                    pos2+=1
                if pos1==left and pos2==right:
                    return right-left
                # the char with charCount<k  seperates the sub string into parts.
                maxLen= max(maxLen,sublongestStr(s,k,pos1,pos2))
                pos1=pos2
            return maxLen
        return sublongestStr(s,k,0,len(s))


if __name__ == '__main__':
    object = Solution()
    s = "ababacb"
    k = 3


    r = object.longestSubstring(s,k)
    print(r)
    print('---End---')
