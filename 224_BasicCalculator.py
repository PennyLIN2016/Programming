class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 182 ms, faster than 32.66% of Python online submissions for Basic Calculator.
        # Memory Usage: 15.2 MB, less than 86.42% of Python online submissions for Basic Calculator.
        # time:o(n) space:(n)
        stack = []
        res = 0
        curStr = '0'
        flag = 0
        # add an end mark
        for c in s+'#':
            if c == '(':
                stack.append(res)
                stack.append(flag)
                res = 0
                flag = 0
            elif c == ')':
                if flag == 0:
                    res += int(curStr)
                else:
                    res -= int(curStr)
                flag = stack.pop()
                oldRes = stack.pop()
                if flag == 0:
                    oldRes += res
                else:
                    oldRes -= res
                res = oldRes
                curStr = '0'
            elif c == '+':
                if flag == 0:
                    res += int(curStr)
                else:
                    res -= int(curStr)
                curStr = '0'
                flag = 0
            elif c == ' ':
                continue
            elif c == '-':
                if flag == 0:
                    res += int(curStr)
                else:
                    res -= int(curStr)
                curStr = '0'
                flag = 1
            elif c == '#':
                if flag == 0:
                    res += int(curStr)
                else:
                    res -= int(curStr)
                flag = 0
            else:
                curStr += c
            print('c: {} stack: {} res: {} flag: {}'.format(c, stack, res, flag))
        return res

obj = Solution()
t1 = "4 - 5"
#t1 = "1-11"
print(t1)
print(obj.calculate(t1))
