class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        #Runtime: 24 ms, faster than 82.58% of Python online submissions for Different Ways to Add Parentheses.
        #Memory Usage: 11.8 MB, less than 76.28% of Python online submissions for Different Ways to Add Parentheses.
        # look each number as a leaf node, the different way to compute is to take different operater as the root node.
        # use dfs to travel all possible ways

        # store the possible compute result in one iteration and return that back to high level call
        res=[]
        # assuming the first and the last char is not char, there is not related description for that scenario in the question.
        for i, value in enumerate(input):
            # get a non-leaf node
            if value =='+' or value =='-' or value =='*' :
                left_res= self.diffWaysToCompute(input[:i])
                right_res= self.diffWaysToCompute(input[i+1:])
                for i in left_res:
                    for j in right_res:
                        if value =='+':
                            res.append(i+j)
                        elif value =='-':
                            res.append(i-j)
                        else:
                            res.append(i*j)
        # no operator in input
        if not res:
            return [int(input)]
        return res





if __name__ == '__main__':
    nums = "2*3-4*5"
    p = Solution()
    print(p.diffWaysToCompute(nums))