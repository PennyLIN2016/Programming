class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # Runtime: 76 ms, faster than 97.93% of Python online submissions for Find Duplicate File in System.
        # Memory Usage: 27.4 MB, less than 50.00% of Python online submissions for Find Duplicate File in System.
        # my own solution: t(n)=o(n*m*k) n len(path) m len(s)
        res=[]
        files=dict()
        for value in paths:
            s=value.split(' ')
            if len(s)<2: continue
            for i in range(1,len(s)):
                sf=s[i].split('.txt')
                if len(sf)!=2:continue
                if sf[1] in files:
                    files[sf[1]].append(s[0]+'/'+sf[0]+'.txt')
                else:
                    files[sf[1]]=[s[0]+'/'+sf[0]+'.txt']
        print(files)
        for key in files:
            if len(files[key])>1:
                res.append(files[key])
        return res
    
    #####python3
        def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        # Runtime: 173 ms, faster than 23.52% of Python3 online submissions for Find Duplicate File in System.
        # Memory Usage: 23.7 MB, less than 84.56% of Python3 online submissions for Find Duplicate File in System.
        # time: o(n: number of files)) space:o(n: number of files)
        import re
        dictPaths = {}
        for v in paths:
            tmp= v.split()
            if len(tmp) == 1:
                continue
            for i in range(1, len(tmp)):
                match = re.findall('([0-9A-Za-z.]+)', tmp[i])
                print('match: {}'.format(match))
                if not match or len(match) != 2:
                    continue
                name, content = match[0], match[1]
                if content in dictPaths:
                    dictPaths[content].append('{}/{}'.format(tmp[0], name))
                else:
                    dictPaths[content]= ['{}/{}'.format(tmp[0], name)]

        print('dictPaths: {}'.format(dictPaths))
        res = []
        for k in dictPaths:
            if len(dictPaths[k]) > 1:
                res.append(dictPaths[k])
        return res

if __name__ == '__main__':
    object = Solution()
    #n1= ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    n1= ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

    print('---Start---')
    print (n1)
    r = object.findDuplicate(n1)
    print(r)
    print('---End---')
