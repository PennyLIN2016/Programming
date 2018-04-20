class Solution(object):

    # a good solution 33s
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # do with the integer part
        ans = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans += str(int(numerator / denominator))
        # do with the fraction part
        if numerator % denominator:
            ans += "."
        numerator =  (numerator % denominator) * 10
        # is an integer
        if numerator == 0:
            return ans

        d = {}# keep the remainder numbers and their indexes where this remainder starts in the res string.
        res = []# keep the string of the fraction
        while True:
            r = numerator % denominator # reminder number
            v = int(numerator / denominator)#integer part
            if numerator in d:# the reminder number repeats , so there is the repeated part
                idx = d[numerator]# get the starting position of the repeated part
                # there are three parts: integer;no-repeated part in fraction; the repeated part in fraction
                return ans + "".join(res[:idx]) + "(" + "".join(res[idx:]) + ")"
            # add the new number into the fraction
            res.append(str(v))
            # keep the index in the res related to the numerator.
            d[numerator] = len(res) - 1
            # go to next loop
            numerator = r * 10
            # the numerator is less than denominator
            if v == 0:
                continue
            # no more reminder , the program finishes
            if r == 0:
                return ans + "".join(res)


if __name__ == '__main__':
    n1 = 17
    n2 = 26

    k = Solution()

    print (k.fractionToDecimal(n1,n2))