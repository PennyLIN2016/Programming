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

    # The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    #用randN生成randM，其中N<M的基本思想是：
    # 首先找到一个能覆盖M整数倍的随机序列，对于此题来说，最少能全覆盖的范围是1~49，即(rand7() - 1) * 7 + rand7()，调用此式子并舍去大于40的数，可以得到1~40的均匀分布
    # 得到了1~40的均匀分布后，接着模10取余即可得到0~9的均匀分布，然后加1即是rand10
    # try to get a random n number, n%10 = 0
    # The return number should be completely random between 1 an 10

    def rand10(self):
        """
        :rtype: int
        """
        # Runtime: 319 ms, faster than 97.15% of Python3 online submissions for Implement Rand10() Using Rand7().
        # Memory Usage: 16.6 MB, less than 78.86% of Python3 online submissions for Implement Rand10() Using Rand7().

        v = (rand7() -1) * 7 + rand7()
        while v > 40:
            v = (rand7() -1) * 7 + rand7()
        return v % 10 + 1

if __name__ == '__main__':
    object = Solution()
    #A=  3
    print('---Start---')
    r = object.rand10()
    print(r)
    print('---End---')
