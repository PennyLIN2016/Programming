class Solution:
    # my solution 44s
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        notation_s = []
        try:
            for value in tokens:
                if value is '+':
                    operand1 = notation_s.pop()
                    operand2 = notation_s.pop()
                    notation_s.append(operand1 + operand2)
                elif value is '-':
                    operand1 = notation_s.pop()
                    operand2 = notation_s.pop()
                    notation_s.append(operand2- operand1)
                elif value is '*':
                    operand1 = notation_s.pop()
                    operand2 = notation_s.pop()
                    notation_s.append(operand1 * operand2)
                elif value is '/':
                    operand1 = notation_s.pop()
                    operand2 = notation_s.pop()
                    notation_s.append(int(operand2/operand1))
                else:
                    notation_s.append(int(value))
        except:
            return 0
        else:
            return notation_s.pop()




if __name__ == '__main__':

    s = ["4","3","-"]

    print (s)

    k = Solution()

    print (k.evalRPN(s))


