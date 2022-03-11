class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 96.07% of Python online submissions for Longest Substring with At Least K Repeating Characters.
        #Memory Usage: 11.8 MB, less than 97.50% of Python online submissions for Longest Substring with At Least K Repeating Characters.
        
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
    
    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Runtime: 20 ms, faster than 93.41% of Python online submissions for Longest Substring with At Least K Repeating Characters.
        # Memory Usage: 13.7 MB, less than 54.40% of Python online submissions for Longest Substring with At Least K Repeating Characters.
        if k > len(s): return 0
        for c in s:
            # if str is the target string is decided by the less occurance char in the string. 
            # if count c less than k, delect the c and check the sub strings splited by the letter.
            if s.count(c)< k:
                return(max(self.longestSubstring(t,k) for t in s.split(c)))
        # all chars in string count more than k
        return len(s)

if __name__ == '__main__':
    object = Solution()
    s = "ababacb"
    k = 3


    r = object.longestSubstring(s,k)
    print(r)
    print('---End---')
