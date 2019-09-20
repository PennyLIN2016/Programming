import string
class Solution(object):
    #Runtime: 640 ms, faster than 11.18% of Python online submissions for License Key Formatting.
    #Memory Usage: 14.2 MB, less than 46.67% of Python online submissions for License Key Formatting.
    # time : o(n)
    def licenseKeyFormatting1(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res=''
        l=1
        for i in range(len(S)-1,-1,-1):
            if S[i]=="-":
                continue
            if l>K:
                res='-'+res
                l=1
            if S[i]<='z' and S[i]>='a':
                tmp=string.upper(S[i])
            else:
                tmp=S[i]
            res= tmp+res
            l+=1
            print res
            print l
            print "------"
        return res

    def licenseKeyFormatting(self, S, K):
        #Runtime: 24 ms, faster than 90.93% of Python online submissions for License Key Formatting.
        #Memory Usage: 14.3 MB, less than 46.67% of Python online submissions for License Key Formatting.
        res=[]
        s=S.upper().split('-')
        s="".join(s)
        L=len(s)
        if L%K!=0:
            res.append(s[:L%K])
        for i in range(L%K,L,K):
            res.append(s[i:i+K])
        return "-".join(res)



if __name__ == '__main__':
    object = Solution()
    A= "--a-a-a-a--"
    K = 2


    print('---Start---')
    r = object.licenseKeyFormatting(A,K)
    print(r)
    print('---End---')
