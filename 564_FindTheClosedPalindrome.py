
class Solution:
    # Runtime: 49 ms, faster than 36.71% of Python3 online submissions for Find the Closest Palindrome.
    # Memory Usage: 14 MB, less than 36.00% of Python3 online submissions for Find the Closest Palindrome.

    # Judge whether + 1 or - 1 changes in digits
    def change_bit(self, n):
        if (len(str(n + 1)) != len(str(n))):
            return 1
        elif ((len(str(n - 1)) != len(str(n))) or (n == 1)):
            return -1
        else:
            return 0

    # Find out the nearest number to n in minnum, midnum and maxnum. If the distance is the same, find the smallest number.
    def find_min(self, minnum, midnum, maxnum, n):
        minabs = abs(int(minnum) - int(n))
        midabs = abs(int(midnum) - int(n))
        maxabs = abs(int(maxnum) - int(n))
        if (midabs <= maxabs):
            if (minabs <= midabs):
                return minnum
            else:
                return midnum
        else:
            if (minabs <= maxabs):
                return minnum
            else:
                return maxnum

    def nearestPalindromic(self, n):
        # Only one digit
        if (len(n) < 2):
            return str(int(n) - 1)
        # The case of even digits
        if ((len(n) % 2) == 0):
            substr_front = n[0:len(n) // 2]
            midnum = substr_front + substr_front[::-1]
            maxsub_front = str(int(substr_front) + 1)
            maxnum = maxsub_front + maxsub_front[::-1]
            minsub_front = str(int(substr_front) - 1)
            minnum = minsub_front + minsub_front[::-1]
        # The case of odd digits
        else:
            substr_front = n[0:(len(n) + 1) // 2]
            midnum = substr_front + (substr_front[::-1])[1:len(substr_front)]
            maxsub_front = str(int(substr_front) + 1)
            maxnum = maxsub_front + (maxsub_front[::-1])[1:len(maxsub_front)]
            minsub_front = str(int(substr_front) - 1)
            minnum = minsub_front + minsub_front[::-1][1:len(minsub_front)]
        # It is the case of palindrome itself, midabs=0, does not meet the requirements, so the midnum is initialized to "0" to achieve the goal that midabs must be greater than max(maxabs,minabs)
        if (midnum == n):
            midnum = "0"
        # The number of digits in plus 1
        if (self.change_bit(int(substr_front)) == 1):
            maxnum = ""
            maxnum = '1' + ((len(n) - 1) * '0') + '1'
        # If the number of digits changes after subtraction 1, be careful to include 1-1=0.
        if (self.change_bit(int(substr_front)) == -1):
            minnum = ""
            minnum = (len(n) - 1) * '9'
        # print(minnum)
        # print(midnum)
        # print(maxnum)
        return self.find_min(minnum, midnum, maxnum, n)

if __name__ == '__main__':

    obj = Solution()
    t1 = "123"

    print('input: {}'.format(t1))
    r = obj.nearestPalindromic(t1)
    print('output: {}'.format(r))