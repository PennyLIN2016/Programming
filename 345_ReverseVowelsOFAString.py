class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 40 ms, faster than 94.43% of Python online submissions for Reverse Vowels of a String.
        #Memory Usage: 14.9 MB, less than 18.35% of Python online submissions for Reverse Vowels of a String.
        # time:o(n) space:o(n)
        if not s: return s
        Vowels={'a','e','i','o','u','A','E','I','O','U'}
        pos_s= []
        res= list(s)
        for i,value in enumerate(s):
            if value in Vowels: pos_s.append(i)
        if pos_s==[]:return s
        l,r = 0,len(pos_s)-1
        while l<r:
            res[pos_s[l]],res[pos_s[r]]=res[pos_s[r]],res[pos_s[l]]
            l+=1
            r-=1
        return ''.join(res)
if __name__ == '__main__':
    k = Solution()
    l= "leetcode"

    r = k.reverseVowels(l)
    print(r)
    print('---End---')



