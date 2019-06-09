class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #Runtime: 36 ms, faster than 65.30% of Python online submissions for Bulls and Cows.
        #Memory Usage: 11.9 MB, less than 13.59% of Python online submissions for Bulls and Cows.
        #time o(n) space: o(n)
        import collections
        if not secret or not guess: return ''
        if len(secret)!=len(guess):return ''
        number= dict(collections.Counter(secret))
        cow,bull=0,0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                number[secret[i]]-=1
                bull+=1
        for i in range(len(guess)):
            if secret[i]!=guess[i] and guess[i]in number.keys()and number[guess[i]]>0:
                cow+=1
                number[guess[i]]-=1
        return str(bull)+'A'+str(cow)+'B'




if __name__ == '__main__':
    k = Solution()
    s = "1807"
    t = "7810"
    r = k.getHint(s,t)

    print(r)
    print('---End---')



