class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 16 ms, faster than 75.41% of Python online submissions for Decode String.
        #Memory Usage: 11.8 MB, less than 62.34% of Python online submissions for Decode String.
        # time:o(n) space: o(n)
        path=[]
        curTime=0
        curStr=''
        for v in s:
            if v.isdigit():
                # for example: "12[a]"
                curTime= curTime*10+int(v)
            elif v=="[":
                path.append(curStr)
                path.append(curTime)
                curTime=0
                curStr=''
            elif v=="]":
                preTime= path.pop()
                preStr= path.pop()
                curStr= preStr+ preTime*curStr
            else:
                curStr+=v
        return curStr

if __name__ == '__main__':
    object = Solution()
    k =  "3[a]2[bc]"


    r = object.decodeString(k)
    print(r)
    print('---End---')
