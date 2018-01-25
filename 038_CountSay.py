class question(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0 or None:
            return ''

        if n == 1:
            return '1'

        r = []
        pre_str = self.countAndSay(n-1)
        i = 0
        while i < len(pre_str):
            count = 1
            j= i+1
            while j< len(pre_str):
                if pre_str[j] == pre_str[i]:
                    count+=1
                    j+= 1
                else:
                    break

            r.append(str(count))
            r.append(pre_str[i])

            i+= count

        return ''.join(r)

if __name__ == '__main__':
    inputs = raw_input('Please input the N:')
    print 'N:',inputs.strip()

    target = int(inputs)
    k = question()
    r= k.countAndSay(target)
    print 'Result: ', r



