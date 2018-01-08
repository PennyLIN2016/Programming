
class question(object):

    def reverse(self, x):
        """
        :type x: int
        :type: return : the returned int
        """
        if abs(x) > 0x7fffffff :
            return 0

        neg_flag = ''
        if x < 0:
            neg_flag = '-'

        s_pos = str(abs(x))
        s_l = []

        for i in range(-1,-len(s_pos)-1,-1):
            s_l.append(s_pos[i])

        s_r = neg_flag + ''.join(s_l)

        if abs(int(s_r))> 0x7fffffff:
            return 0
        else:
            return int(s_r)



if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs.strip()
    #r = k.LongestPaliSubstring(inputs.strip())
    r = k.reverse(int(inputs))
    print  'Result : ',r


