class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)< 2:
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left:left+1].upper()!= s[right:right+1].upper():
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':

    #inputs = "A man, a plan, a canal: Panama"
    inputs ='a,'


    k = Solution()
    r = k.isPalindrome(inputs)

    print r
