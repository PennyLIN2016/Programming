class Solution(object):
    def palindromecheck(self,sub_str):
        if len(sub_str)<2:
            return True
        start = 0
        end= len(sub_str)-1
        while start<end:
            if sub_str[start] != sub_str[end]:
                return False
            start+=1
            end-= 1
        return True

    def next_part(self,s,sub_list):
        if len(s)== 0:
            Solution.r.append(sub_list)
        for i in xrange(1,len(s)+1):
            if self.palindromecheck(s[:i]):
                self.next_part(s[i:],sub_list+[s[:i]])


    def partition(self,s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.r = []
        self.next_part(s,[])
        return Solution.r


if __name__ == '__main__':

    s = 'aab'
    #s = 'bb'

    k = Solution()
    print s
    r= k.partition(s)
    print r
