class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Runtime: 108 ms, faster than 82.07% of Python online submissions for Basic Calculator II.
        #Memory Usage: 14.1 MB, less than 60.55% of Python online submissions for Basic Calculator II.
        if not s: return 0
        num_s=[]
        pre_operator = "+"
        num=0
        for i,value in enumerate(s):
            if value.isdigit():
                num = num*10+ int(value)
            if value in '+-*/' or i== len(s)-1:
                if pre_operator=='+':
                    num_s.append(num)
                elif pre_operator=='-':
                    num_s.append(-num)
                elif pre_operator=="*":
                    num_s.append(num*num_s.pop())
                elif pre_operator=="/":
                    tmp = num_s.pop()
                    if tmp<0:
                        num_s.append(-int(abs(tmp)/num))
                    else:
                        num_s.append(tmp//num)
                pre_operator=value
                num = 0
        return sum(num_s)


if __name__ == '__main__':

    s="0-21"

    object = Solution()
    r = object.calculate(s)

    print(r)
    print('---End---')

