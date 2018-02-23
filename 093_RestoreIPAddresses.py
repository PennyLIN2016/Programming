
class question(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def ValidNums(sub_s):
            # check is the sub_s is valid for a field of Ip
            # the outside loop makes sure the length of sub_s is less than 3
            if len(sub_s)== 1:
                return True
            if len(sub_s)> 1 and sub_s[0]!= '0' and int(sub_s)<256:
                return True
            return False

        r = []
        l = len(s)
        for i in xrange(min(3,l-3)):
            # a is the first field, the len is from 1 to 3.
            # make sure there are at less 3 bits left for the back fields.
            a = s[:i+1]
            if not ValidNums(a):
                break;
            for j in xrange(i+1,min(i+4,l-2)):
                b = s[i+1:j+1]
                if not ValidNums(b):
                    break
                for k in xrange(j+1,min(j+4,l-1)):
                    c = s[j+1:k+1]
                    d = s[k+1:]
                    if not ValidNums(c):
                        break
                    if not ValidNums(d):
                        # keep trying the next valid c. so do not break the loop now ,just skip to next k
                        continue

                    r.append('{}.{}.{}.{}'.format(a,b,c,d))
        return r



if __name__ == '__main__':
    inputs = '0000'
    k = question()
    r = k.restoreIpAddresses(inputs)
    print r





