
class question(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)== 0:
            return []
        dict ={1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        def pickup_letters(s_nums,index,s_tmp,s_r,dict):
            # this function is an iteration for finish a full match.
            if index == len(s_nums):
            #at the end of the string
                s_r.append("".join(s_tmp))
                return

            digit = int(s_nums[index])
            for value in dict.get(digit,[]):
                s_tmp.append(value)
                pickup_letters(s_nums,index+1,s_tmp,s_r,dict)
                s_tmp.pop()

        s_r =[]
        s_tmp= [] # to keep the current matching.
        pickup_letters(digits,0,s_tmp,s_r,dict)
        return s_r


if __name__ == '__main__':

    inputs = '34'
    k = question()
    print 'Input :', inputs
    r = k.letterCombinations(inputs,)
    print  'Result : ',r



