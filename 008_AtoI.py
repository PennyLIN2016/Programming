
class question(object):

    def myAtoi(self, str):
        """
        :type str :str
        :rtype : int
        """
        try:
            i = int(str)
            return i
        except ValueError:
            print 'The str %s is wrong inpouts!'%str
            return 0

    def myAtoiLC(self, str):
        '''
        meet requirements in LEETCODE :
        '''
        s = str.strip()
        if s =='':
            return 0

        if s[0] =='-':
            neg_mark = 1
            tmp = s[1:]
        elif s[0] =='+':
            neg_mark = 0
            tmp = s[1:]
        else:
            neg_mark = 0
            tmp = s[:]

        int_num = 0
        for value in tmp:
            if not value.isdigit():
                break
            int_num = int_num*10 + int(value)

        if neg_mark == 0:
            int_num = min(int_num,2147483647)
        else:
            int_num = max(int_num*-1,-2147483648)

        return int_num



if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs
    r = k.myAtoiLC(inputs)
    #r = k.myAtoi(inputs)
    print  'Result : ',r



