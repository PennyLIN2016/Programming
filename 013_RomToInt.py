
class question(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_num = s.strip()
        num = 0
        for i in range(len(s_num)):
            if s_num[i] == 'I':
                num = num +1
            elif s_num[i] == 'V':
                if i> 0 and s_num[i-1] =='I':
                    num= num+3
                else:
                    num = num+5
            elif s_num[i] == 'X':
                if i>0 and s_num[i-1 ]=='I':
                    num = num+8
                else:
                    num = num+10
            elif s_num[i] == 'L':
                if i> 0 and s_num[i-1] =='X':
                    num += 30
                else:
                    num+= 50
            elif s_num[i]=='C':
                if i> 0 and s_num[i-1] =='X':
                    num += 80
                else:
                    num+= 100
            elif s_num[i]=='D':
                if i> 0 and s_num[i-1] =='C':
                    num += 300
                else:
                    num += 500
            elif s_num[i] == 'M':
                if i> 0 and s_num[i-1] =='C':
                    num += 800
                else:
                    num += 1000
            else:
                print 'there is an error '
                return 0
        return num

    def romanToInt1(self, s):# The same function.
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V": 5, "X":10,"L":50,"C":100, "D":500, "M":1000}
        ans = 0
        for i in xrange(0, len(s) - 1):
            c = s[i]
            cafter = s[i + 1]
            if d[c] < d[cafter]:
                ans -= d[c]
            else:
                ans += d[c]
        ans += d[s[-1]]
        return ans

if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs
    r = k.romanToInt(inputs)
    print  'Result : ',r



