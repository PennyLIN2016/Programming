class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # Runtime: 36 ms, faster than 82.39% of Python3 online submissions for Text Justification.
        # Memory Usage: 14 MB, less than 54.34% of Python3 online submissions for Text Justification.
        # time: o(n) space:o(maxWidth)
        i = 0
        print(len('a  computer.  Art is'))
        curLen, curStr= 0, []
        res = []
        while i < len(words):
            print('i: {} words[i]: {} curLen: {} res: {} curStr: {}'.format(i, words[i], curLen, res, curStr))
            curLen += len(words[i])
            if curLen + len(curStr) == maxWidth:
                print(1)
                curStr.append(words[i])
                res.append(' '.join(curStr))
                i += 1
                curLen = 0
                curStr = []
            elif curLen + len(curStr) > maxWidth:
                print('2')
                curLen -= len(words[i])
                if len(curStr) == 1:
                    tmp = curStr[0] + ' ' * (maxWidth - curLen)
                else:
                    n, m = divmod((maxWidth - curLen), len(curStr)-1)
                    tmp = curStr[0]
                    for j in range(1, len(curStr)):
                        if j <= m:
                            tmp += ' '*(n+1) + curStr[j]
                        else:
                            tmp += ' '*n + curStr[j]
                res.append(tmp)
                print('res: {} curLen: {}'.format(res,curLen))
                curLen = 0
                curStr = []
            else:
                print('3')
                curStr.append(words[i])
                i += 1
        if curStr:
            tmp = ' '.join(curStr)
            res.append(tmp + ' ' * (maxWidth - len(tmp)))
        return res






if __name__ == '__main__':
    obj = Solution()
    t1 = ["What","must","be","acknowledgment","shall","be"]
    t2 = 16
    print('input: {}'.format(t1))
    r = obj.fullJustify(t1, t2)
    print('output: {}'.format(r))
    print('--------END--------')