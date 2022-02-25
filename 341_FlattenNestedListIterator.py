# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
#Runtime: 68 ms, faster than 84.85% of Python online submissions for Flatten Nested List Iterator.
#Memory Usage: 17.6 MB, less than 24.23% of Python online submissions for Flatten Nested List Iterator.
import collections
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = collections.deque()
        def getFlat(nests):
            for value in nests:
                if value.isInteger():
                    self.list.append(value.getInteger())
                else :
                    getFlat(value.getList())
        getFlat(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.list.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


## solution 2:
#Runtime: 63 ms, faster than 92.18% of Python online submissions for Flatten Nested List Iterator.
#Memory Usage: 19.1 MB, less than 81.84% of Python online submissions for Flatten Nested List Iterator.
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self._list = []
        self._cursor = 0
        self.getList(nestedList)

    def getList(self, list):

        for v in list:
            if v.isInteger():
                self._list.append(v.getInteger())
            else:
                self.getList(v.getList())

    def next(self):
        """
        :rtype: int
        """
        self._cursor += 1
        return self._list[self._cursor-1]
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self._cursor != len(self._list)


if __name__ == '__main__':
    l= [[1,1],2,[1,1]]
    i, v = NestedIterator(l), []
    while i.hasNext(): v.append(i.next())
    print(v)
    print('---End---')



