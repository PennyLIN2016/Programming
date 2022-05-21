class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #Runtime: 12 ms, faster than 93.17% of Python online submissions for Detect Capital.
        #Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Detect Capital.
        if not word or len(word)==1: return True
        tmp=word
        if word[0].islower() :
            if tmp==word.lower():return True
            else:
                return False
        else:
            if tmp[1:]==tmp[1:].lower() or tmp[1:]==tmp[1:].upper():
                return True
            else:
                return False

    def detectCapitalUse(self, word: str) -> bool:
        # Runtime: 32 ms, faster than 84.79% of Python3 online submissions for Detect Capital.
        # Memory Usage: 13.9 MB, less than 54.30% of Python3 online submissions for Detect Capital.
        # time: o(n) space: o(1)
        if ord('A') <= ord(word[0]) <= ord('Z'):
            start = 1
        else:
            start = 0
        flag = None
        for i in range(start, len(word)):

            if not flag:
                if ord('A') <= ord(word[i]) <= ord('Z'):
                    flag = 'Upper'
                else:
                    flag = 'lower'
            else:
                if flag == 'Upper' and ord('a') <= ord(word[i]) <= ord('z'):
                    return False
                elif flag == 'lower' and ord('A') <= ord(word[i]) <= ord('Z'):
                    return False
        return True

if __name__ == '__main__':
    object = Solution()
    A= 'Dgogle'


    print('---Start---')
    print A
    r = object.detectCapitalUse(A)
    #12701
    print(r)
    print('---End---')
