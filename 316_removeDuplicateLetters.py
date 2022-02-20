class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        # Greedy solution: time: o(n) space:o(1) 26 letters
        # Save the latest occurrence of letters
        lastPos = {c:i for i, c in enumerate(s)}
        # save the letters selected
        inSet = set()
        # '' is the smaller than any letter
        # keep a stack for selected letter in order
        # save the smallest str at current pos
        curStack = []
        for i ,c in enumerate(s):
            # curStack saves the smallest str at current pos
            # in the loop, only curStack[-1] can be removed
            # c < curStack[-1] make sure the letters in curStack[:-2] should already be optimized.
            if c in inSet:
                continue
            # if c not in inSet, add it into curStack: : make sure the result includes all letters
            # two conditions to remove curStack[-1]
            # the c is smaller than curStack[-1]: curStack[-1] should behind of c
            # curStack[-1] will occur later: make sure the result includes all letters
            # curStack saves the smallest list in pos(i-1), so just compare the letter in pos(i-1)
            while curStack and c < curStack[-1] and lastPos[curStack[-1]] > i:
                inSet.remove(curStack.pop())
            curStack.append(c)
            inSet.add(c)
            print('curStack: {} inSet: {}'.format(curStack, inSet))
        return ''.join(curStack[1:])

if __name__ == '__main__':
    k = Solution()
    s =  "cbacdcbc"
    r = k.removeDuplicateLetters(s)

    print(r)
    print('---End---')
