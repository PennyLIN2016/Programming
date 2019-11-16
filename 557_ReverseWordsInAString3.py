class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 40 ms, faster than 39.42% of Python online submissions for Reverse Words in a String III.
        #Memory Usage: 13 MB, less than 63.64% of Python online submissions for Reverse Words in a String III.
        # my solution: time: o(n) space: 0(n)
        if not s: return s
        chars= s.split(' ')
        for i in range(len(chars)):
            chars[i] = self.reverseStr(chars[i])
        return " ".join(chars)

    def reverseStr(self,word):
        tmp = list(word)
        tmp=tmp[::-1]

        return ''.join(tmp)




if __name__ == '__main__':
    object = Solution()
    #n1= [1000,100,10,2]
    n1="Let's take LeetCode contest"

    print('---Start---')
    print n1
    r = object.reverseWords(n1)
    print(r)
    print('---End---')
