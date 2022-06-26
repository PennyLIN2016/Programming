class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # Runtime: 693 ms, faster than 14.96% of Python online submissions for Find Words That Can Be Formed by Characters.
        # Memory Usage: 14.2 MB, less than 51.97% of Python online submissions for Find Words That Can Be Formed by Characters.
        # time:o(len(chars)+len(words)*len(word)) space: o(len(chars)+len(word))
        import collections
        cnt = collections.Counter(chars)
        res = 0
        for word in words:
            tmp = collections.Counter(word)
            #print('tmp: {} cnt: {} cnt-tmp: {}'.format(tmp, cnt, cnt-tmp))
            if all([tmp[c] <= cnt[c] for c in tmp]):
                print(word)
                res += len(word)
        return res

obj = Solution()
t1 = ["cat", "bt", "hat", "tree"]
t2 = "atach"
print(obj.countCharacters(t1, t2))
