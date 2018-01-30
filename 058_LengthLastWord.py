
class question(object):# low efficiency but can return the longest string, not just the length.
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s =='':
            return 0
        list_s = s.split()
        return len(list_s[-1])

if __name__ == '__main__':

    s1 ='Hello World    '

    print 'Input : ',s1
    k = question()
    r = k.lengthOfLastWord(s1)
    print  'Result : ',r


