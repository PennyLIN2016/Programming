class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #Runtime: 80 ms, faster than 83.71% of Python online submissions for Queue Reconstruction by Height.
        #Memory Usage: 12.1 MB, less than 65.91% of Python online submissions for Queue Reconstruction by Height.
        # other`s solution
        # sort the list by h and index.
        # the taller ones in the front
        
        # the smaller value would not break the rule, so should make sure the higher people position before
        # insert a value.
        # for the same value, just insert the people in v[1]ascend order
        # people should be sorted by v[0] descended order and by v[1]ascend order
        
        people.sort(key = lambda x:(-x[0],x[1]))
        res=[]
        for p in people:
            # the smaller ones will not affect the index of taller ones.
            # when smaller ones inserted in front of taller people, that will not affect the index of taller ones(here, the previous elements in res are taller people)
            res.insert(p[1],p)
        return res



if __name__ == '__main__':
    object = Solution()
    num = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    print(num)
    r = object.reconstructQueue(num)
    #print(r)
    print('---End---')
