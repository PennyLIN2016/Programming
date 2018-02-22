class question(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
       """
        if s == '':
            return 0

        # r[i] save the decoding num of s[:i]
        r= [0]*(len(s)+1)
        r[0] = 1 # this is a seed for '10' or '20'
        # '0 'can repersent a letter alone.
        r[1] = 0 if s[0]=='0'else 1
        for i in xrange(2,len(r)):
            if s[i-1] == '0':
                if s[i-2] == '2' or s[i-2]== '1':
                    # there is one decoding type s[i-1]+s[i]
                    r[i]= r[i-2]
                else:
                    return 0
            elif s[i-2]=='1'or (s[i-2])=='2'and int(s[i-1])<= 6:
                # there are two choices
                r[i] = r[i-1]+r[i-2]
            else:
                # only one choice
                r[i]= r[i-1]
        return r[-1]


if __name__ == '__main__':

    inputs = '00'
    k = question()
    r = k.numDecodings(inputs.strip())
    print  'result : ',r


