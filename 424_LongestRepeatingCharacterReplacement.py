class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Runtime: 104 ms, faster than 67.12% of Python online submissions for Longest Repeating Character Replacement.
        # Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Longest Repeating Character Replacement.
        # sliding window solution: time o(n) space: o(1)
        if not s: return 0
        if len(s)<=k+1: return len(s)
        # keep the max len of repeating letter , the input only includes upper case letter,
        map_list= [0]*26
        slow,fast,maxLen,res=0,0,0,0
        while(fast<len(s)):
            cur_fast= s[fast]
            fast += 1
            map_list[ord(cur_fast)-ord('A')]+=1
            # the maxLen comes from map_list[], so will not be greater than the real maxlen of repeating letter
            # get most common vlaue count
            maxLen=max(maxLen,map_list[ord(cur_fast)-ord('A')])
            #the gap can not be covered by k
            while(fast-slow-maxLen>k):
                # the sliding window is greater , slide the slow to
                map_list[ord(s[slow]) - ord('A')]-=1
                slow += 1
            res= max(res,fast-slow)

        return res

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Runtime: 594 ms, faster than 5.02% of Python online submissions for Longest Repeating Character Replacement.
        # Memory Usage: 13.7 MB, less than 70.30% of Python online submissions for Longest Repeating Character Replacement.
        # sliding window problem: two pointer solution
        # time: o(n) space: o(n)
        n = len(s)
        # an empty counter object
        c = collections.Counter()
        res = 0
        # two pointer, [left, right] is the sub string required
        left, right = 0,0
        while right< n:
            c[s[right]]+=1
            # can't meet the requirement
            # downsize the window to ensure the window satisfied.
            while right-left+1 -c.most_common(1)[0][1]>k:
                c[s[left]] -= 1
                left += 1
            # update the current max result
            res = max(res, right-left+1)
            right += 1
        return res


if __name__ == '__main__':

    #s= "ABAB"
    #k = 2
    s = "AABABBA"
    k = 1
    #s= "ABAA"
    #k=0
    p = Solution()
    
    print (s)
    print('-------start------')
    print(p.characterReplacement(s,k))
