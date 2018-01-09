
class question(object):

    def IsPalindrome(self, x):
        """
        :type x :int
        :rtype : bool
        """
        if x < 0:
        # the negative number is not palindrome.
            return False

        s = str(x)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False

            i +=1
            j -=1
        return True


if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs
    r = k.IsPalindrome(int(inputs))
    print  'Result : ',r



