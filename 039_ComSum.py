class question(object):
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combinationSum_next(can,pos,next_target,tmp,r):
            if next_target == 0:
                return r.append(tmp+[])

            for i in xrange(pos,len(can)):
                if (next_target -candidates[i])>= 0 :
                    #the number of candidates should be more than 0
                    tmp.append(candidates[i])
                    combinationSum_next(can,i,(next_target -candidates[i]),tmp,r)
                    tmp.pop()



        if not candidates:
            return None

        tmp = []
        r = []
        combinationSum_next(candidates,0,target,tmp,r)
        return  r

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start, target, path, res):
            if target == 0:
                return res.append(path + [])

            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                if target >= candidates[i]:
                    path.append(candidates[i])
                    dfs(candidates, i, target - candidates[i], path, res)
                    path.pop()

        candidates.sort()
        res = []
        dfs(candidates, 0, target, [], res)
        return res
    
    def combinationSum(self, candidates, target)://faster than 93.92%
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, start, target, path, res):
            if target == 0:
                return res.append(path + [])

            for i in range(start, len(candidates)):

                if target >= candidates[i]:
                    path.append(candidates[i])
                    dfs(candidates, i, target - candidates[i], path, res)
                    path.pop()
                else:
                    break
        candidates.sort()
        res = []
        dfs(candidates, 0, target, [], res)
        return res

if __name__ == '__main__':
    #List = [1,2,3,6,7,9,10]
    #List = [8,7,6,5,4,3,2,1]
    #List = [1,2,3,7,0,9,4,10,9,8,6]
    #List = None
    #List = [1,2,3,4,5]
    List = [2,2]

    target = 4
    k = question()
    print 'input is :',List
    r= k.combinationSum(List,target)
    print r







