# Below is the interface for Iterator, which is already defined for you.
#Runtime: 16 ms, faster than 98.05% of Python online submissions for Peeking Iterator.
#Memory Usage: 12 MB, less than 5.40% of Python online submissions for Peeking Iterator.
# based on the existing clsass iterator  implement a new class to support peek(),next().hasnext()
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.list= nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.list!=[]

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

        if len(self.list)==0: return None
        elif len(self.list)==1:
            tmp=self.list[0]
            self.list=[]
        else:
            tmp = self.list[-1]
            self.list = self.list[:-2]
        return tmp
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itertor = iterator
        self.nextvalue= None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.nextvalue==None:
            self.nextvalue = self.itertor.next()
        return self.nextvalue


    def next(self):
        """
        :rtype: int
        """
        if self.nextvalue!=None:
            tmp= self.nextvalue
            self.nextvalue= None
            return tmp
        else:
            return self.itertor.next()


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nextvalue!=None:
            return True
        else:
            return self.itertor.hasNext()

if __name__ == '__main__':
    nums=[1,2,3]
    # Your PeekingIterator object will be instantiated and called as such:
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()   # Get the next element but not advance the iterator.
        print(val)
        iter.next()         # Should return the same value as [val].


    print('---End---')

