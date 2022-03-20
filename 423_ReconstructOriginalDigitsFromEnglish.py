import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 356 ms, faster than 8.74% of Python online submissions for Reconstruct Original Digits from English.
        #Memory Usage: 12.4 MB, less than 50.00% of Python online submissions for Reconstruct Original Digits from English.
        # other`s solution: to be analyzed
        s_counter= collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        # 6, 0, 2, 8, 7 have unqiue special chars. so check them and remove them firstly
 
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        # count occurance of 0-9
        res=[0]*10
        for i,value in enumerate(nums):
            n_counter=numc[i]
            t=min(s_counter[c]/n_counter[c] for c in n_counter)
            res[digits[i]]=t
            for j in range(t):
                s_counter.subtract(n_counter)
        return ''.join(str(i)*n for i,n in enumerate(res))
    
   def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 101 ms, faster than 54.46% of Python online submissions for Reconstruct Original Digits from English.
        # Memory Usage: 13.9 MB, less than 87.50% of Python online submissions for Reconstruct Original Digits from English.
        # time: o(n) space: o(n)
        ct = collections.Counter(s)
        #print(ct)
        # get the count based on special char
        res = {
            # only o has "z" so ct["z"] is the num of "0"
            0: ct["z"],
            # one: zero, two, four
            1: ct["o"] - ct["z"] - ct["w"] - ct["u"],
            # two:
            2: ct["w"],
            # three: two, eight
            3: ct["t"] - ct["w"] - ct["g"],
            # four
            4: ct['u'],
            # five: four, five
            5: ct['f']- ct['u'],
            # six
            6:ct['x'],
            # seven: six
            7: ct["s"] - ct["x"],
            # eight
            8: ct["g"],
            # nine: six eight five
            9:  ct["i"] - ct["x"] - ct["g"] - ct["f"] + ct["u"],
        }
        return "".join(str(k) * v for k,v in res.items())

if __name__ == '__main__':
    object = Solution()
    num = "owoztneoer"

    print(num)
    print('---Start---')
    r = object.originalDigits(num)
    print(r)
    print('---End---')
