
class question(object):
    def IsPaliStr(self,s):
        """
        :type s: str
        :type: return : boolean if the str is palindromic, return True, otherwise return False
        """
        j = -1

        for i in range (int(len(s)/2)):
            if s[i]!= s[j]:
                return False
            j-=1
        return True


    def LongestPaliSubstring(self, s):## low efficiency
        """
        :type s: str
        :type: return : the longest palindromic substring in s
        """
        if len(s)<1:
            return ''

        for l in range(len(s),1,-1):

            for i in range (len(s)-l+1):

                substr = s[i:(i+l)]
                if self.IsPaliStr(substr):
                    return (substr)

        return s[0]

    def longestPalindrome(self, s):# passed by leetcode
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            if 2 * (n - i) + 1 < right - left + 1:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return s[left:right + 1]

if __name__ == '__main__':

    inputs = raw_input('input the string :  ')
    k = question()
    print 'Input :', inputs.strip()
    #r = k.LongestPaliSubstring(inputs.strip())
    r = k.longestPalindrome(inputs.strip())
    print  'Result : ',r


