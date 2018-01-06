
class question(object):# low efficiency but can return the longest string, not just the length.
    def Longstr(self,s):
        """
        :type s: str
        :type: return : string
        """
        if s =='':
            return 0
        index = 0
        lengS = 1

        for  i  in  range (len(s)):
            if len(s)-i > lengS:
                tmps= []
                tmps.append(s[i])
                flag = 1
                j = i+1
                while flag and j < len(s):
                    if s[j] in tmps:
                        flag = 0
                    else:
                        tmps.append(s[j])
                        j+= 1

                if j-i > lengS:
                    index = i
                    lengS = len(tmps)

        return lengS

    def lengthOfLongestSubstring(self, s):## high efficiency
        d = {}
        start = 0
        length = 0
        for i,c in enumerate(s):
            if c in d:
            # if finding the repeated c, the longest str begains form the first letter after the repeated c.
                start = max(start, d[c] + 1)
            d[c] = i
            length = max(length, i - start + 1)
        return length

if __name__ == '__main__':

    inputs = raw_input('input the string :  ')
    k = question()
    print 'input :', inputs.strip()
    r = k.lengthOfLongestSubstring(inputs.strip())
    print  'result : ',r


