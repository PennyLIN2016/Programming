class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        #Runtime: 8 ms, faster than 98.66% of Python online submissions for Longest Absolute File Path.
        #Memory Usage: 11.9 MB, less than 38.09% of Python online submissions for Longest Absolute File Path.
        # time : o(n) space:O(n)

        if not input:return 0
        max_l= 0
        # o(n)
        sDir= input.split('\n')
        path=[]
        for v1 in sDir:
            cur_level=0
            while cur_level<len(v1):
                if v1[cur_level] == '\t':
                    cur_level+=1
                    continue
                tmp=v1[cur_level:]
                if '.'in v1:
                    # the len of tmp: cur_level is for '\'
                    max_l= max(max_l,len(tmp)+sum(path[:cur_level])+cur_level)
                else:
                    if len(path)>=cur_level+1:
                        path[cur_level]=len(tmp)
                    else:
                        path.append(len(tmp))
                break
        return max_l
    
    def lengthLongestPath1(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Runtime: 10 ms, faster than 99.45% of Python online submissions for Longest Absolute File Path.
        #Memory Usage: 13.6 MB, less than 70.17% of Python online submissions for Longest Absolute File Path.
        # time: o(n*k) space: o(n) n: path number, k: the lever number
        dirList = input.split('\n')
        stackLen = []
        res = float('-inf')
        for v in dirList:
            num = v.count('\t')
            while len(stackLen) >num:
                stackLen.pop()
            v = v.split('\t')[-1]
            stackLen.append(len(v))
            if '.' in v:
                # the path should add '/'between folder
                res = max(res, sum(stackLen)+num)
                stackLen.pop()
        return 0 if res == float('-inf') else res

if __name__ == '__main__':
    object = Solution()
    k = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    r = object.lengthLongestPath(k)
    print(r)
    print('---End---')
