class Solution(object):
    # my solution 43s
    # equits to  return " ".join(s.split()[::-1])
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if use s.split(' ') the result will be wrong.
        l = s.split()
        right = len(l)-1
        left = 0
        while right > left:
            l[right],l[left] = l[left], l[right]
            right -= 1
            left += 1

        return ' '.join(l)

if __name__ == '__main__':

    s = "     Showing translation for initialization   "

    print (s)

    k = Solution()

    print (k.reverseWords(s))



