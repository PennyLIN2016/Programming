# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

def rand7():
    import random
    return random.randint(1,7)


#Runtime: 408 ms, faster than 41.09% of Python online submissions for Implement Rand10() Using Rand7().
#Memory Usage: 17 MB, less than 100.00% of Python online submissions for Implement Rand10() Using Rand7().
    # class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        return self.rand40()%10+1

    def rand49(self):
        return 7*(rand7()-1)+rand7()-1

    def rand40(self):
        num=self.rand49()
        while num>=40:
            num=self.rand49()
        return num


if __name__ == '__main__':
    object = Solution()
    #A=  3
    print('---Start---')
    r = object.rand10()
    print(r)
    print('---End---')
