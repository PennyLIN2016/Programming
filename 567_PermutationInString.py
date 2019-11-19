import collections
class Solution(object):
    def checkInclusion1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #76 / 103 test cases passed. time out
        # my own solution: time : o(w1*w2)
        w1, w2, = len(s1), len(s2)
        if w2<w1:return False
        c1=collections.Counter(s1)
        s2=list(s2)
        for i in range(0,w2-w1+1,1):
            cCur=collections.Counter(s2[i:i+w1])
            if cCur&c1==c1:return True
        return False

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #Runtime: 88 ms, faster than 30.75% of Python online submissions for Permutation in String.
        #Memory Usage: 12 MB, less than 58.33% of Python online submissions for Permutation in String.
        # google solution: time 0(max(w1,w2)) space: o(w1)
        # improved points based on solution1: in the w1 window , do not use counter (o(w1)), just add/subtract the previous counter(o(1))
        w1, w2, = len(s1), len(s2)
        if w2 < w1: return False
        c1 = collections.Counter(s1)
        s2 = list(s2)
        c2=collections.Counter(s2[:w1-1])
        left,right=0,w1-1
        while right<w2:
            c2[s2[right]]+=1
            if c2==c1:return True
            c2[s2[left]]-=1
            if c2[s2[left]]==0:
                del c2[s2[left]]
            right+=1
            left+=1
        return False



if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 = s1 = "adc"

    n2= "dcda"


    print('---Start---')
    print (n1)
    r = object.checkInclusion(n1,n2)
    print(r)
    print('---End---')