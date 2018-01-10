
class question(object):

    def intToRoman1(self, num):
        '''
        :type num: int < 3999
        :rtype: str
        '''

        dict =  [["","I","II","III","IV","V","VI","VII","VIII","IX"],
                            ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                            ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                            ['','M','MM','MMM']]
        s = []
        tmp = num
        while tmp!= 0:
            s.append((tmp%10))
            tmp = int(tmp/10)

        s_rom = []
        for i in range(len(s)):
            s_rom.append(dict[i][s[i]])
        s_rom.reverse()
        return ''.join(s_rom)


    def intToRoman(self, num):
        '''
        :type num: int < 3999
        :rtype: str
        '''

        dict =  [["","I","II","III","IV","V","VI","VII","VIII","IX"],
                            ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                            ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                            ['','M','MM','MMM']]
        s = []
        s.append(dict[3][int(num/1000)])
        s.append(dict[2][int((num/100))%10])
        s.append(dict[1][int((num/10))%10])
        s.append(dict[0][num%10])

        r = ''.join(s)
        return r.strip()

if __name__ == '__main__':

    inputs = raw_input('input the integer :  ')
    k = question()
    print 'Input :', inputs
    r = k.intToRoman(int(inputs))
    print  'Result : ',r



