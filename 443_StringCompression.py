class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #Runtime: 32 ms, faster than 98.95% of Python online submissions for String Compression.
        #Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for String Compression.
        # time: o(n) space:o(1)
        if not chars: return 0
        newI,preI,pre,pre_count=1,1,chars[0],1
        for i in range(1,len(chars)):
            print('i:'+str(i) +'  chars[i]:'+str(chars[i]))
            print('count:'+str(pre_count))
            print('newI:'+str(newI))

            if chars[i]!=pre:
                pre=chars[i]
                if pre_count>1:
                    tmp=str(pre_count)
                    chars[newI:newI+len(tmp)]=tmp
                    newI+=len(tmp)

                chars[newI]=chars[i]
                newI+=1
                pre_count=1
            else:
                pre_count+=1
        if pre_count>1:
            tmp=str(pre_count)
            chars[newI:newI+len(tmp)]=tmp
            newI+=len(tmp)

        while len(chars)>newI:chars.pop()
        print chars
        return newI



if __name__ == '__main__':
    object = Solution()
    num =  ["b","b","b","b","b","b","b","b","b","b","b","a","a","c"]
    #num=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    #num="abab"
    #p="ab"

    print(num)
    print('---Start---')
    r = object.compress(num)
    print(r)
    print('---End---')
