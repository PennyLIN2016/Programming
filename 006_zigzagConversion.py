
class question(object):

    def zigzagconversion(self, s, rownum):
        """
        :type s: str in zigzag format
        :type s: rownum
        :type: return : s in display order (line by line)
        """
        if rownum <= 1:
            return s

        size = 2*rownum-2
        r_s = []
        l = len(s)

        for i in range (rownum):# put the char into the str by line
            p = i
            k = -i
            while p < l or k < l:# the pos is in the range of s
                if 0 <= k <l and p!= k and i != rownum-1:
                # the middle lines, with two elements in a row
                    r_s.append(s[k])
                if p < l:
                    r_s.append(s[p])
                # go to next block
                p += size
                k += size

        return ''.join(r_s)


if __name__ == '__main__':

    inputs = raw_input('input the string :  ')
    k = question()
    print 'Input :', inputs.strip()
    #r = k.LongestPaliSubstring(inputs.strip())
    r = k.zigzagconversion(inputs.strip(),3)
    print  'Result : ',r


