
class question(object):# low efficiency but can return the longest string, not just the length.
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)< len(needle):
            return -1
        if len(needle)==0:
            return 0

        pos= 0
        i= 0
        while i < len(haystack):
            if haystack[i] == needle[pos]:
                if pos == len(needle)-1:
                    return i-pos
                pos+=1
                i+=1
                continue
            else:
                i = i - pos + 1
                pos = 0

        return -1

if __name__ == '__main__':

    s1 ='mississippi'
    s2 = 'issip'
    print 'the input : ',s1,
    print 'the needdle :', s2
    k = question()
    r = k.strStr(s1,s2)
    print  'result : ',r


