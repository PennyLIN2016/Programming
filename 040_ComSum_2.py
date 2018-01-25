class question(object):
     def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combinationSum_next(candidates, pos,target,r,tmp,set_in):
            if target == 0:
                r.append(tmp+[])
                return

            for i in xrange(pos,len(candidates)):
                if i > pos and candidates[i]==candidates[i-1]:
                    continue
                if target < candidates[i] :
                    return
                if i not in set_in:
                    set_in.add(i)
                    tmp.append(candidates[i])
                    combinationSum_next(candidates, i+1,target - candidates[i],r,tmp,set_in)
                    tmp.pop()
                    set_in.discard(i)

        candidates.sort()
        r = []
        tmp =[]
        set_in = set()
        combinationSum_next(candidates, 0,target,r,tmp,set_in)
        return r

if __name__ == '__main__':
    #List = [1,2,3,6,7,9,10]
    #List = [8,7,6,5,4,3,2,1]
    #List = [1,2,3,7,0,9,4,10,9,8,6]
    #List = None
    #List = [1,2,3,4,5]
    List = [10, 1, 2, 7, 6, 1, 5]

    target = 8
    k = question()
    print 'input is :',List
    r= k.combinationSum2(List,target)
    print r







