class RandomizedSet(object):
    # Runtime: 460 ms, faster than 84.08% of Python online submissions for Insert Delete GetRandom O(1).
    # Memory Usage: 59.5 MB, less than 29.94% of Python online submissions for Insert Delete GetRandom O(1).
    def __init__(self):
        self._dict = {}
        self._list = []


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self._dict:
            return False
        # len() : time: o(1)
        self._dict[val] = len(self._list)
        self._list.append(val)
        print('self._list: {} self._dict: {}'.format(self._list, self._dict))
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self._dict:
            return False
        pos, lastValue = self._dict[val], self._list[-1]
        self._dict[lastValue] = pos
        self._list[pos], self._list[-1] = lastValue, self._list[pos]
        del self._list[-1]
        del self._dict[val]
        print('self._list: {} self._dict: {}'.format(self._list, self._dict))
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        print('self._list: {} self._dict: {}'.format(self._list, self._dict))
        import random
        return random.choice(self._list)

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())


