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

        def licenseKeyFormatting1(self, s: str, k: int) -> str:
        # misunderstanding with the question:
        # In this solution, keep the first frag without dash if the len(frag) < k
        # the question is to split the chars (without dash) in to k-length flags,
        # if the length of the chars mods k is not zero, keep the extra ones in the first frag.
        temp = s.upper().split('-')
        res, left = '', []
        for i in range(len(temp)):
            if temp[i] == '':
                continue
            if len(temp[i]) <= k:
                res = temp[i]
                if i == len(temp)-1:
                    left = ''
                else:
                    left = ''.join(temp[i+1:])
            else:
                res = temp[i][:k]
                if i == len(temp) - 1:
                    left = ''.join([temp[i][k:]])
                else:
                    left = ''.join([temp[i][k:]] + temp[i:])
            break
        print('left- {} res: {}'.format(left, res))
        if left == '':
            return res
        start = 0
        while start + k -1 < len(left):
            res += '-' + left[start:start + k]
            start += k
        if start < len(left) - 1:
            res += '-' + left[start:]
        return res

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Runtime: 60 ms, faster than 68.59% of Python3 online submissions for License Key Formatting.
        # Memory Usage: 14.6 MB, less than 47.51% of Python3 online submissions for License Key Formatting.
        # time: o(n)
        res=[]
        tmp= ''.join(s.upper().split('-'))
        print('tmp: {}'.format(tmp))
        l = len(tmp)
        if l % k != 0:
            res.append(tmp[:l%k])
        print('res: {}'.format(res))
        for i in range(int(l/k)):
            res.append(tmp[l%k + i * k: l%k + (i+1)*k])
        print('res2- {}'.format(res))
        return '-'.join(res)


if __name__ == '__main__':
    object = Solution()
    A= "--a-a-a-a--"
    K = 2


    print('---Start---')
    r = object.licenseKeyFormatting(A,K)
    print(r)
    print('---End---')
