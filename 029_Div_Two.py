class question(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 0x7fffffff
        if divisor == 0:
            return MAX_INT
        neg_flag =0
        if dividend < 0 and divisor >0 :
            neg_flag =1
        if dividend> 0 and divisor< 0 :
            neg_flag =1

        a = abs(dividend)
        b = abs(divisor)
        T = 1
        sub_tmp= b
        r = 0

        while a>= b:
            while (sub_tmp <<1) <= a:
                T<<=1
                sub_tmp<<=1
            r += T
            T = 1
            a -= sub_tmp
            sub_tmp = b

        if neg_flag == 1:
            return(max(-1*r,-2147483648))
        else:
            return min(r,MAX_INT)



if __name__ == '__main__':
    k = question()

    r= k.divide(0x7fffffff,-1)
    print r



