import random
class Solution(object):
    #Runtime: 244 ms, faster than 90.89% of Python online submissions for Shuffle an Array.
    #Memory Usage: 17.2 MB, less than 95.32% of Python online submissions for Shuffle an Array.

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = self.original[:]
        random.shuffle(tmp)
        return tmp
    
    def shuffle2(self):
        """
        :rtype: List[int]
        """
        #Runtime: 344 ms, faster than 51.60% of Python online submissions for Shuffle an Array.
        #Memory Usage: 19.6 MB, less than 51.41% of Python online submissions for Shuffle an Array.
        import random
        indexs = [i for i in range(len(self._original))]

        res = []
        for _ in range(len(self._original)):
            index = random.choice(indexs)
            res.append(self._original[index])
            indexs.remove(index)
            
        return res



# Your Solution object will be instantiated and called as such:
nums= [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
