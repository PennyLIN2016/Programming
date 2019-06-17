class NumArray1(object):
    # in leetcoode timeout: brutal solution

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums= nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        if not self.nums or len(self.nums)<=i: return
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums or len(self.nums)<=j:
            return 0
        tmpSum=0
        for k in range(i,j+1):
            tmpSum+= self.nums[k]
        return tmpSum

class NumArray(object):
    ##Runtime: 136 ms, faster than 63.52% of Python online submissions for Range Sum Query - Mutable.
    #Memory Usage: 16.3 MB, less than 39.50% of Python online submissions for Range Sum Query - Mutable.
    # use special binary tree to store the sum[i]. for odd number: the sum[i]= nums[i]. for even number: sum[i] = sum[k]+sum[p]
    # k ,p are the numbers: k+ lowbit()= i. lowbit: the rightest 1 bit . for example: lowbit(100)=4, lowbit(111)=1
    def __init__(self,nums):
        self.sumArray=[0]*(len(nums)+1)
        self.nums= nums
        self.l = len(nums)
        for i in range(self.l):

            self.add(i+1,nums[i])

    def add(self,pos,val):
        while pos<=self.l:
            self.sumArray[pos]+=val
            # get the next pos include the sum[pos]
            pos+=self.lowbit(pos)

    def lowbit(self,pos):
        # the computer always store number in complement number. x&-x can get the rightest "1" bit number
        return pos&-pos

    def sum(self,pos):
        res= 0
        while pos>0:
            res+= self.sumArray[pos]
            pos-=self.lowbit(pos)
        return res

    def update(self,i ,val):

        self.add(i+1,val-self.nums[i])
        self.nums[i]=val

    def sumRange(self,i,j):
        if not self.nums: return 0
        return self.sum(j+1)-self.sum(i)




if __name__ == '__main__':
    s= [1, 3, 5]

    p = NumArray(s)
    r1=p.sumRange(0,2)
    print(r1)
    print('update that...')
    p.update(1,2)
    print(p.sumRange(0,2))