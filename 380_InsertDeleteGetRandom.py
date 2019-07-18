import random
class RandomizedSet(object):
#Runtime: 92 ms, faster than 92.49% of Python online submissions for Insert Delete GetRandom O(1).
#Memory Usage: 16.5 MB, less than 26.75% of Python online submissions for Insert Delete GetRandom O(1).
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums,self.pos= [],{}



    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        else:
            self.nums.append(val)
            self.pos[val]= len(self.nums)-1
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        else:
            i,tail=self.pos[val],self.nums[-1]
            self.nums[i]= tail
            self.pos[tail]=i
            self.pos.pop(val,0)
            self.nums.pop()
            return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = random.randint(0,len(self.nums)-1)
        return self.nums[i]





if __name__ == '__main__':
    object = RandomizedSet()
    for i in range(8):
        param_1 = object.insert(i*2)
    param_2 = object.remove(6)
    param_3 = object.getRandom()

    print(param_3)

    print('---End---')
